# -*- coding: utf-8 -*-
"""
Create by sandy at 14:46 28/03/2022
Description: ToDo
"""
import json
import logging

from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from application import settings
from frames.utils.request_util import get_request_ip, get_request_data, get_request_path, get_request_user, \
    get_login_location, get_browser, get_os, get_verbose_name

logger = logging.getLogger(__name__)


class ApiLoggingMiddleware(MiddlewareMixin):
    """
    用于记录API访问日志中间件
    """

    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.enable = getattr(settings, 'API_LOG_ENABLE', None) or False
        self.methods = getattr(settings, 'API_LOG_METHODS', None) or set()

    @classmethod
    def __handle_request(cls, request):
        request.request_ip = get_request_ip(request)
        request.request_data = get_request_data(request)
        request.request_path = get_request_path(request)

    @classmethod
    def __handle_response(cls, request, response):
        # request_data,request_ip由PermissionInterfaceMiddleware中间件中添加的属性
        body = getattr(request, 'request_data', {})
        # 请求含有password则用*替换掉(暂时先用于所有接口的password请求参数)
        if isinstance(body, dict) and body.get('password', ''):
            body['password'] = '*' * len(body['password'])

        if not hasattr(response, 'data') or not isinstance(response.data, dict):
            response.data = {}

        if not response.data and response.content:
            try:
                content = json.loads(response.content.decode())
                response.data = content if isinstance(content, dict) else {}
            except Exception as error:
                logger.info(error)
                pass

        user = get_request_user(request)
        info = {
            'request_ip': getattr(request, 'request_ip', 'unknown'),
            'creator': user if not isinstance(user, AnonymousUser) else None,
            'dept_belong_id': getattr(request.user, 'dept_id', None),
            'request_method': request.method,
            'request_path': request.request_path,
            'request_body': body,
            'response_code': response.data.get('code'),
            'request_location': get_login_location(request),
            'request_os': get_os(request),
            'request_browser': get_browser(request),
            'request_msg': request.session.get('request_msg'),
            'status': True if response.data.get('code') in [200, 204] else False,
            'json_result': {"code": response.data.get('code'), "msg": response.data.get('msg')},
            'request_modular': request.session.get('model_name'),
        }
        logger.info(info)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(view_func, 'cls') and hasattr(view_func.cls, 'queryset'):
            request.session['model_name'] = get_verbose_name(view_func.cls.queryset)
        return

    def process_request(self, request):
        self.__handle_request(request)

    def process_response(self, request, response):
        """
        主要请求处理完之后记录
        :param request:
        :param response:
        :return:
        """
        if self.enable:
            if self.methods == 'ALL' or request.method in self.methods:
                self.__handle_response(request, response)
        return response
