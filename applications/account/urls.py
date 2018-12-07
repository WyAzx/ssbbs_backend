from django.urls import path
from account.views.login import LoginView

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
