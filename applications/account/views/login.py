import logging

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from account.models import SsUser
from account.serializers import UserDetailSerializer
from utils.common import get_random_id
from utils.send_requests import get_wechat_openid
from utils.shortcuts import get_random_user_name

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

            user_data = UserDetailSerializer(user).data
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = Response({'code': 200, 'data': {'user': user_data, 'token': 'JWT {}'.format(token)}})
        else:
            response = Response({'msg': 'wrong_type', 'code': 801})
        return response
