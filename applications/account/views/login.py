import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from account.models import SsUser
from account.serializers import UserDetailSerializer
from exception.exceptions import UserNotExistError, PasswordWrongError
from utils.common import get_random_id, get_verify_phone_key, get_verify_email_key
from utils.send_requests import get_wechat_openid
from utils.shortcuts import get_random_user_name, verify_code

LOG = logging.getLogger(__name__)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        login_type = request.data.get('login_type')
        if login_type == '0':
            code = request.data.get('code')
            nick_name = request.data.get('nick_name')
            avatar_url = request.data.get('avatar_url')
            gender = request.data.get('gender')

            wechat_id = get_wechat_openid(code)

            user_id = str(get_random_id())
            user_name = get_random_user_name()
            user, ok = SsUser.objects.get_or_create(
                defaults={'id': user_id, 'nick_name': nick_name, 'gender': int(gender), 'user_name': user_name,
                          'wechat_avatar': avatar_url},
                wechat_id=wechat_id)
        elif login_type == '1':
            phone = request.data.get('phone')
            code = request.data.get('code')
            code_key = get_verify_phone_key(phone)

            verify_code(code_key, code)

            user_id = str(get_random_id())
            user_name = get_random_user_name()
            user, ok = SsUser.objects.get_or_create(
                defaults={'id': user_id, 'user_name': user_name},
                phone=phone)
        elif login_type == '2':
            email = request.data.get('email')
            code = request.data.get('code')
            code_key = get_verify_email_key(email)

            verify_code(code_key, code)

            user_id = str(get_random_id())
            user_name = get_random_user_name()
            user, ok = SsUser.objects.get_or_create(
                defaults={'id': user_id, 'user_name': user_name},
                email=email)

        elif login_type == '3':
            phone = request.data.get('phone')
            password = request.data.get('password')
            try:
                user = SsUser.objects.get(phone=phone)
            except ObjectDoesNotExist:
                raise UserNotExistError()
            if not user.check_password(password):
                raise PasswordWrongError()

        elif login_type == '4':
            email = request.data.get('email')
            password = request.data.get('password')
            try:
                user = SsUser.objects.get(email=email)
            except ObjectDoesNotExist:
                raise UserNotExistError()
            if not user.check_password(password):
                raise PasswordWrongError()

        else:
            return Response({'msg': 'wrong_type', 'code': 801})

        user_data = UserDetailSerializer(user).data
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = Response({'code': 200, 'data': {'user': user_data, 'token': 'JWT {}'.format(token)}})

        return response
