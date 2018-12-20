from rest_framework import serializers

from account.verify import ParamVerify


class AddThreadVerify(ParamVerify):
    fid = serializers.IntegerField()
    subject = serializers.CharField()
    message = serializers.CharField()
