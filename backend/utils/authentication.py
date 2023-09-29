from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import NotAuthenticated

from utils.jwt import check_jwt


class JWTAuthentication(BaseAuthentication):
    """JWT Auth"""
    
    @classmethod
    def get_ip_address(self, request):
        """Get IP address"""
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
        
        if not ip:
            ip = request.META.get('REMOTE_ADDR')
        
        client_ip = ip.split(',')[-1].strip() if ip else ip

        return client_ip

    def authenticate(self, request):
        # get token from header
        jwt = request._request.headers.get('Authorization')

        if not jwt:
            return None

        is_valid, result = check_jwt(jwt)

        if not is_valid: 
            return None

        return result, jwt

    def authenticate_header(self, request):
        return super().authenticate_header(request)


class LoginRequiredAuthentication(JWTAuthentication):
    """Need auth"""

    def authenticate(self, request):
        result = super().authenticate(request)

        if result is None:
            raise NotAuthenticated(detail='Аутентификация сәтсіз аяқталды')
        
        return result

    def authenticate_header(self, request):
        return super().authenticate_header(request)