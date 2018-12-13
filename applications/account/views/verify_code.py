import logging

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from account.verify import VerifyCodeVerify
from auth.authentication import JSONWebTokenAuthentication
from utils.shortcuts import send_verify_email

LOG = logging.getLogger(__name__)


class VerifyCodeView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self, request):
        verify = VerifyCodeVerify(data=request.data)
        verify.is_valid(raise_exception=True)
        send_type = verify.data.get('type')
        if send_type == 1:
            phone = verify.data.get('value')
            # response = SNS().send_message(phone)
            # LOG.info('sns send response : {}'.format(response))
        elif send_type == 2:
            mail = verify.data.get('value')
            send_verify_email(mail)
        return Response({'code': 0, 'message': 'success'})
