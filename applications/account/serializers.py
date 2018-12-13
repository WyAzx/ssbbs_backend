from rest_framework import serializers

from account.models import SsUser


class UserDetailSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        temp = data.copy()
        for k, v in temp.items():
            if v is None:
                data.pop(k, None)
        if 'avatar' in data:
            pass
        elif 'wechat_avatar' in data:
            data['avatar'] = data.pop('wechat_avatar')
        # if 'avatar' in data:
        #     data['avatar'] = get_avatar_url(data['avatar'])
        return data

    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

    class Meta:
        model = SsUser
        fields = '__all__'
