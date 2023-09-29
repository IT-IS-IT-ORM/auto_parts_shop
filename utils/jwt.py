from django.conf import settings
from jwt import encode as jwt_encode,decode as jwt_decode, ExpiredSignatureError

from datetime import datetime, timedelta, timezone

from user.models import User

jwt_config = {
    'key': settings.SECRET_KEY,
    'exp': (datetime.now(tz=timezone.utc) + timedelta(days=30*6)).timestamp(),
    'algorithm': 'HS256'
}

def create_jwt(payload: dict) -> str:
    '''
    Crea JWT, payload is: { uid: User.id }
    '''
    payload['exp'] = jwt_config['exp']

    return jwt_encode(payload, key=jwt_config['key'], algorithm=jwt_config['algorithm'])


def check_jwt(encoded: str):
    '''
    Check JWT, return user model object
    '''

    try:
        payload = jwt_decode(encoded, key=jwt_config['key'], algorithms=[jwt_config['algorithm']])
    except ExpiredSignatureError:
        # Token expires
        return False, 'Авторизацияның мерзімі аяқталды, жүйеге қайта кіріңіз'
    except Exception:
        # Pseudo-token!
        return False, 'Авторизация қабылданбады, қайта кіріңіз'

    user = User.objects.get(id=payload['uid'])

    return True, user