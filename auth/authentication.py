# import logging
#
# from django.contrib.auth import get_user_model
# from rest_framework import HTTP_HEADER_ENCODING
# from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#
# LOG = logging.getLogger(__name__)
#
#
# def get_authorization_header(request):
#     """
#     Return request's 'Authorization:' header, as a bytestring.
#
#     Hide some test client ickyness where the header can be unicode.
#     """
#     auth = request.META.get('HTTP_AUTHORIZATION')
#     if isinstance(auth, str):
#         # Work around django test client oddness
#         auth = auth.encode(HTTP_HEADER_ENCODING)
#     return auth
#
#
# class JSONWebTokenAuthentication(BaseAuthentication):
#
#     www_authenticate_realm = 'api'
#
#     def authenticate(self, request):
#         token = self.get_token_value(request)
#         if token is None:
#             raise ParamMissError(key='Authorization')
#         if not isinstance(token, str):
#             token = token.decode(HTTP_HEADER_ENCODING)
#         if token == "":
#             return None
#         try:
#             payload = decode_handler(token)
#         except jwt.ExpiredSignature:
#             raise ExpiredSignature()
#         except jwt.DecodeError:
#             raise AuthenticationFailed(_('Error decoding token.'))
#         except jwt.InvalidTokenError:
#             raise InvalidTokenError()
#
#         user = self.authenticate_credentials(payload)
#         now = datetime.utcnow()
#         redis_db = get_redis_client()
#         last_operation_key = get_last_operation_key(user.id)
#         limit = timedelta(seconds=operation_update_interval)
#         if not redis_db.get(last_operation_key) or now - datetime.fromtimestamp(float(redis_db.get(last_operation_key))) > limit:
#             user.last_operation_time = now
#             user.save()
#             cache_operation_time(last_operation_key, now.timestamp(), redis_db)
#         return user, token
#
#     def authenticate_credentials(self, payload):
#         User = get_user_model()
#         user_id = payload.get('user_id')
#         if not user_id:
#             raise AuthenticationFailed(_('Invalid payload.'), 2203)
#
#         try:
#             user = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             raise AuthenticationFailed(_('Invalid token.'), 2203)
#
#         if not user.is_active:
#             raise AuthenticationFailed(_('User account is disabled.'), 2202)
#
#         return user
#
#     def authenticate_header(self, request):
#         return 'Basic realm="%s"' % self.www_authenticate_realm
#
#     def get_token_value(self, request):
#         token = get_authorization_header(request)
#         return token
