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

    class Meta:
        model = SsUser
        fields = '__all__'
