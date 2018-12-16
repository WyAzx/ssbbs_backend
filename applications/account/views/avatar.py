from rest_framework.views import APIView
from rest_framework.response import Response

from account.verify import AvatarUploadVerify


class AvatarView(APIView):
    def post(self, request):
        verify = AvatarUploadVerify(data=request.data)
        verify.is_valid(raise_exception=True)
        avatar = verify.data.get('avatar')

