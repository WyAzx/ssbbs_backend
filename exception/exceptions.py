from rest_framework import status
from rest_framework.exceptions import APIException


class CustomAPIException(APIException):
    status_code = status.HTTP_200_OK


class ParamMissError(CustomAPIException):
    def __init__(self, key=None, detail=None):
        self.detail = {
            'message': detail if detail else _('%(key)s: This field is required.') % {'key': key},
            'code': 1001
        }


class ParamIllegalError(CustomAPIException):
    def __init__(self, key=None, detail=None):
        self.detail = {
            'message': detail if detail else _('%(key)s: Param illegal.') % {'key': key},
            'code': 1002
        }


class UserNotExistError(CustomAPIException):
    def __init__(self, detail=None):
        self.detail = {
            'message': detail if detail else _("User doesn't exist!"),
            'code': 2001
        }


class WeChatConnectError(CustomAPIException):
    def __init__(self, detail=None):
        self.detail = {
            'message': detail,
            'code': 3001
        }


class VerifyCodeError(CustomAPIException):
    def __init__(self, detail=None):
        self.detail = {
            'message': detail,
            'code': 3010
        }
