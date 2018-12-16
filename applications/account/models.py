from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    pass


class SsUser(AbstractBaseUser):
    id = models.CharField(primary_key=True, max_length=36)
    password = models.CharField(max_length=200)
    st_id = models.CharField(max_length=10, blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    nick_name = models.CharField(max_length=32, blank=True, null=True)
    user_name = models.CharField(max_length=32, unique=True)
    avatar = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=8, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    role = models.IntegerField(default=0)
    wechat_id = models.CharField(max_length=28, blank=True, null=True)
    group = models.IntegerField(default=0)
    last_login = models.DateTimeField(db_column='last_login_time')
    wechat_avatar = models.CharField(max_length=256, blank=True, null=True)

    USERNAME_FIELD = 'user_name'

    objects = UserManager()

    @property
    def is_active(self):
        return self.role != -1

    class Meta:
        managed = False
        db_table = 'ss_user'


class SsUserCode(models.Model):
    code = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'ss_user_code'

