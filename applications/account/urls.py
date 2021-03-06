from django.urls import path
from account.views.login import LoginView
from account.views.user_info import UserInfoView
from account.views.verify_code import VerifyCodeView
from rest_framework_jwt.views import refresh_jwt_token

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify code'),
    path('info/', UserInfoView.as_view(), name='user info'),
    path('token/', refresh_jwt_token, name='token'),
]
