import datetime
import logging
import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty

from exception.exceptions import ParamMissError, ParamIllegalError

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
