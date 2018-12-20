from django.urls import path

from forum.views.thread import ThreadView

app_name = 'forum'

urlpatterns = [
    path('thread/', ThreadView.as_view(), name='thread'),
]
