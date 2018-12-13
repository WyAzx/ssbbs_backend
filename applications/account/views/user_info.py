from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import UserDetailSerializer


class UserInfoView(APIView):
    def get(self):
        serializer = UserDetailSerializer(self.request.user)
        user_data = serializer.data
        return Response({'code': 0, 'data': user_data})
