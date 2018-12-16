import datetime
import logging
import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty

from account.models import SsUser
from exception.exceptions import ParamMissError, ParamIllegalError, UserInfoUpdateError

LOG = logging.getLogger(__name__)


class ParamVerify(serializers.Serializer):

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        return None

    def run_validation(self, data=empty):
        try:
            return super().run_validation(data)
        except ValidationError as e:
            raise ParamMissError(detail=e.detail)


class VerifyCodeVerify(ParamVerify):
    type = serializers.IntegerField()
    value = serializers.CharField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['type'] == 1:
            if not data.get('value'):
                raise ParamMissError(key="phone")
        elif data['type'] == 2:
            if not data.get('value'):
                raise ParamMissError(key="mail")
        else:
            raise ParamIllegalError(key="type")
        return data


class UserInfoUpdateVerify(ParamVerify):
    password = serializers.CharField(allow_null=True, max_length=16)
    user_name = serializers.CharField(allow_null=True, max_length=32)
    nick_name = serializers.CharField(allow_null=True, max_length=32)
    birthday = serializers.DateField(allow_null=True)
    gender = serializers.IntegerField(allow_null=True, min_value=0, max_value=2)
    description = serializers.CharField(allow_null=True, max_length=256)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_name = data.get('user_name')
        if SsUser.objects.get(user_name=user_name):
            raise UserInfoUpdateError(detail='user name has existed')


class AvatarUploadVerify(ParamVerify):
    avatar = serializers.ListField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        avatars = data.get('avatar')
        data['avatar'] = avatars[0]
        return data

    def validate(self, data):
        avatars = data.get('avatar')
        if avatars is None:
            raise ParamMissError(key="avatar")
        if len(avatars) != 1:
            raise ParamIllegalError(key="avatar")
        return data
