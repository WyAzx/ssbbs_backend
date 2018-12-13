from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import UserDetailSerializer
from account.utils import get_update_data
from account.verify import UserInfoUpdateVerify


class UserInfoView(APIView):
    def get(self, request):
        serializer = UserDetailSerializer(self.request.user)
        user_data = serializer.data
        return Response({'code': 0, 'data': user_data})

    def post(self, request):
        verify = UserInfoUpdateVerify(data=self.request.data)
        data = get_update_data(verify.data)
        if len(data) == 0:
            serializer = UserDetailSerializer(self.request.user)
        else:
            serializer = UserDetailSerializer(self.request.user, data, partial=True)
            serializer.is_valid()
            serializer.save()
        return Response({'code': 0, 'data': serializer.data})
