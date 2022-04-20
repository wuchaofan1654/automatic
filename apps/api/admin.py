from django.contrib import admin

# Register your models here.

from .models import Api, Param, Validator, Extractor, Result, Report, Project


class ApiAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'method', 'key_yn')
    search_fields = ('key_yn', 'status')


class ParamAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'type', 'require')
    search_fields = ('type',)


class ValidatorAdmin(admin.ModelAdmin):
    list_display = ('expression', 'expression_type', 'excepted', 'symbol')
    search_fields = ('expression_type',)


class ExtractorAdmin(admin.ModelAdmin):
    list_display = ('expression', 'expression_type', 'variable')
    search_fields = ('expression_type',)


admin.site.register(Api, ApiAdmin)
admin.site.register(Param, ParamAdmin)
admin.site.register(Validator, ValidatorAdmin)
admin.site.register(Extractor, ExtractorAdmin)
admin.site.register(Result)
admin.site.register(Report)
admin.site.register(Project)
