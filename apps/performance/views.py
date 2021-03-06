from frames.response import SuccessResponse, ErrorResponse
from frames.viewsets import CustomModelViewSet
from .filters import PublishFilter, ModuleFilter
from .instances import CompareResult, SingleCompareResult
from .models import Publish, Module
from .serializers import PublishSerializer, PublishCreateUpdateSerializer, ModuleSerializer, ModuleStatSerializer
from .services.module import ModuleDataFitLineChart
from .signals import sync_modules_by_publish


class PublishModelViewSet(CustomModelViewSet):
    """
    模型的CRUD视图
    """
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
    create_serializer_class = PublishCreateUpdateSerializer
    update_serializer_class = PublishCreateUpdateSerializer
    filter_class = PublishFilter
    ordering = '-create_datetime'  # 默认排序

    @classmethod
    def compareByPk(cls, request, *args, **kwargs):
        try:
            pk1 = kwargs.get('pk1')
            pk2 = kwargs.get('pk2')

            pk1_modules = Module.objects.filter(publish__id=int(pk1))
            pk2_modules = Module.objects.filter(publish__id=int(pk2))

            data = CompareResult(
                pk1_publish=PublishSerializer(Publish.objects.get(pk=int(pk1))).data,
                pk2_publish=PublishSerializer(Publish.objects.get(pk=int(pk2))).data
            )

            for module in pk1_modules:
                result = SingleCompareResult(module_name=module.module_name, pk1_module_size=module.module_size)
                for _module in pk2_modules:
                    if _module.module_name == result.module_name:
                        result.pk2_module_size = _module.module_size
                data.results.append(result.calculate_diff())

            diff_modules = [_module for _module in pk2_modules if _module.module_name
                            not in [module.module_name for module in pk1_modules]]

            data.results.extend(
                [SingleCompareResult(
                    module_name=module.module_name,
                    pk2_module_size=module.module_size).calculate_diff() for module in diff_modules])

            return SuccessResponse(data.sort_by_diff().dict())
        except Exception as err:
            return ErrorResponse(code=201, msg=f'{err}')

    @classmethod
    def buildOptions(cls, request):
        query_sets = Publish.objects.all()
        query_sets = [{'id': query.id, 'version': query.version} for query in query_sets]
        return SuccessResponse(query_sets)

    @classmethod
    def syncModules(cls, request, pk):
        try:
            publish = Publish.objects.get(pk=pk)
            sync_modules_by_publish(publish)
            return SuccessResponse(msg='同步成功')

        except Exception as error:
            return ErrorResponse(code=10002, msg=error)


class ModuleModelViewSet(CustomModelViewSet):
    """
    模型的CRUD视图
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_class = ModuleFilter
    ordering = '-create_datetime'  # 默认排序

    @classmethod
    def nameOptions(cls, request):
        queryset = Module.objects.all()
        result = {}
        for query in queryset:
            if query in result.keys():
                continue

            result[query.module_name] = query

        results = [{"id": res.id, "name": res.module_name} for res in result.values()]

        return SuccessResponse(results)

    @classmethod
    def moduleStat(cls, request):
        queryset = Module.objects.all()
        module_name_set = list(set([query['module_name'] for query in queryset.values('module_name')][:20]))

        results = {
            module_name:
                {r['publish']['version']: r.get('module_size', 0)
                 for r in ModuleStatSerializer(queryset.filter(module_name=module_name), many=True).data}
            for module_name in module_name_set}

        return SuccessResponse(ModuleDataFitLineChart(results).result)
