from django.http.response import JsonResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_202_ACCEPTED,HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

class ResponseFormatMiddleware:
    '''统一响应数据的格式'''

    def __init__(self, get_response):
        self.get_response = get_response
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response_template = self.response_template
    
        # [DRF] Error
        if isinstance(response, Response):
            if response.status_code not in (HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT):
                response_template['is_ok'] = False
                if response.data:
                    response_template = { **response_template, **response.data }
                else:
                    response_template = { **response_template }
            # [DRF] Success
            else:
                '''
                DRF 返回数据的格式: { ... } 或 [ ... ]
                自定义返回的格式: { data: ..., Formatted: 非None值 }
                最终返回的格式: { data: ..., ... }
                **response_template**
                '''

                if isinstance(response.data, dict) and response.data.get('Formatted') is None:
                    response.data = { 'data': response.data }
                elif not isinstance(response.data, dict):
                    response.data = { 'data': response.data }

                # 合并数据, 组成模板返回
                response_template = { **response_template, **response.data }
        # [Django] Success
        elif isinstance(response, (TemplateResponse, HttpResponseRedirect)):
            return response
        # [Django] Error
        else:
            response_template['is_ok'] = False
            # 404
            if response.status_code == HTTP_404_NOT_FOUND:
                response_template['message'] = 'Ресурс жоқ'
            # 500 +
            elif int(response.status_code) >= 500:
                response_template['message'] = 'Серверлік ерекше жағдай'
            # 静态文件访问
            else:
                return response
            
        return JsonResponse(data=response_template, status=response.status_code)

    @property
    def response_template(self):
        return {
        'is_ok': True,
        're_login': False,
        'data': None,
        'message': ''
    }