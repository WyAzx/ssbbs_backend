import logging

from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import UserDetailSerializer

LOG = logging.getLogger(__name__)


class PasswordView(APIView):

    def post(self):
        password = self.request.data.get('password')
        serializer = UserDetailSerializer(self.request.user, {"password": password}, partial=True)
        serializer.is_valid()
        serializer.save()
        LOG.info("user [{}] change password".format(self.request.user.id))
        return Response({'code': 0, 'data': serializer.data})


