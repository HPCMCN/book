```python
# -*- coding:utf-8 -*-
# author: HPCM
# time: 2021/11/2 15:57
# file: login.py
import string
import random
from hashlib import md5
from datetime import datetime

import jwt
from rest_framework import exceptions
from rest_framework.settings import api_settings
from django.utils.translation import ugettext as _
from django.contrib.auth.backends import ModelBackend
# noinspection PyUnresolvedReferences,PyDeprecation
from rest_framework_jwt.utils import jwt_payload_handler as base_jwt_payload_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication as BaseJSONWebTokenAuthentication, \
    jwt_decode_handler

from users import models


class JSONWebTokenAuthentication(BaseJSONWebTokenAuthentication):
    """validate token"""

    def authenticate(self, request):
        jwt_value = self.get_jwt_value(request)
        if jwt_value is None:
            return None
        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()
        user = self.authenticate_credentials(payload)
        if not user.lived_state or md5(user.password.encode()).hexdigest()[:5] != payload["md"]:
            msg = _('Signature has expired.')
            raise exceptions.AuthenticationFailed(msg)
        return user, jwt_value


class JSONThirdTokenAuthentication(BaseJSONWebTokenAuthentication):

    def authenticate(self, request):
        token = request.headers.get("token") or request.data and request.data.get("token")
        expired_msg = _("Token has expired.")
        if not token:
            msg = _("Not found token")
            raise exceptions.AuthenticationFailed(msg)
        try:
            token = models.ThirdTokens.objects.get(token=token, is_active=True)
            ct = datetime.now()
            if not token.lived_state or token.start_time > ct or token.end_time and token.end_time < ct:
                raise exceptions.AuthenticationFailed(expired_msg)
        except models.ThirdTokens.DoesNotExist:
            raise exceptions.AuthenticationFailed(expired_msg)
        return token, None


# noinspection PyUnresolvedReferences
class UserValidateBackend(ModelBackend):
    """validate user login"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = self.get_user(username)
        if user and user.lived_state and user.check_password(password):
            user.update_last_time()
            return user

    def get_user(self, username):
        return models.Users.objects.filter(is_active=True, email=username).first()


# noinspection PyDeprecation
def jwt_payload_handler(user):
    payload = base_jwt_payload_handler(user)
    payload["md"] = md5(user.password.encode()).hexdigest()[:5]
    user.last_login = datetime.now()
    user.save()
    return payload


def jwt_response_payload_handler(token, user=None, request=None):
    return {"token": token, "uid": user.id}


def generate_token(user):
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def generate_access_token():
    return "".join(random.sample(string.ascii_letters + string.digits, 32))

```

