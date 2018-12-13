from django.urls import path
from account.views.login import LoginView
from account.views.verify_code import VerifyCodeView

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify code'),
]
