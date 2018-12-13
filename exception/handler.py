from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import set_rollback
from rest_framework.response import Response

from exception.exceptions import CustomAPIException


def api_exception_handler(exc, context=None):

    if isinstance(exc, CustomAPIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, list):
            data = ' '.join(exc.detail)
        elif isinstance(exc.detail, dict):
            if isinstance(exc.detail['message'], dict):
                message = ""
                for k, v in exc.detail['message'].items():
                    if isinstance(v, str):
                        value = v
                    elif isinstance(v, list):
                        value = v[0]
                    else:
                        value = str(v)
                    message += "{}: {} ".format(k, value)
                exc.detail['message'] = message
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        set_rollback()
        return Response(data, status=status.HTTP_200_OK, headers=headers)

    elif isinstance(exc, Http404):
        msg = 'Not found.'
        data = {'detail': msg}

        set_rollback()
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = 'Permission denied.'
        data = {'detail': msg}

        set_rollback()
        return Response(data, status=status.HTTP_200_OK)

    elif isinstance(exc, NotAuthenticated):
        msg = "Authentication credentials were not provided."
        data = {'message': msg, 'code': "2202"}
        set_rollback()
        return Response(data, status=status.HTTP_200_OK)

    elif isinstance(exc, APIException):
        msg = exc.detail
        data = {'message': msg, 'code': "1001"}
        set_rollback()
        return Response(data, status=status.HTTP_200_OK)

    return None

