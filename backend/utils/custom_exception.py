from rest_framework.views import set_rollback, Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.exceptions import (
    APIException,
    ValidationError,
    ParseError,
    PermissionDenied,
    Throttled
)


def custom_exception_handler(exc, context):
    """
    note: `context` is
    { 'view': <app.views.SomeView object at 0x000001E4A1AD1D00>,
      'args': (), 'kwargs': {},
      'request': <rest_framework.request.Request: POST '/api/somethings/'> }
    """
    
    print('custom exception handler\nerror detail: \n', getattr(exc, 'detail', 'no detail'), '\n\n')

    # деректері кері қайтару
    set_rollback()

    if isinstance(exc, ValidationError):
        for value in exc.detail.values():
            return Response(data={'message': str(value[0])}, status=HTTP_400_BAD_REQUEST)

    if isinstance(exc, ParseError):
        return Response(data={'message': 'Деректер заңды json формат емес'}, status=HTTP_400_BAD_REQUEST)

    if isinstance(exc, PermissionDenied):
        exc = PermissionDenied(detail='Рұқсат жеткіліксіз')

    if isinstance(exc, Throttled):
        headers = {
            'Retry-After': exc.wait
        }

        return Response(data={'message': f'Сервер қарбалас'}, status=exc.status_code, headers=headers)

    if isinstance(exc, APIException):
        headers = {}

        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'message': exc.detail}

        return Response(data, status=exc.status_code, headers=headers)

    if isinstance(exc, CustomException):
        return Response(data=exc.data, status=exc.status)

    return None


class CustomException(Exception):
    """Return format for unifying exceptions"""

    def __init__(
        self,
        # error message
        message: str,
        # data
        data=None,
        # response status code
        status_code=HTTP_400_BAD_REQUEST,
    ):

        self.message = message
        self.status = status_code
        if data is None:
            self.data = {'message': message}
        else:
            self.data = data

    def __str__(self):
        return self.message