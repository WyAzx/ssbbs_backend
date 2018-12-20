import datetime
import time

import pytz
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response

from forum.models import SsForumThread, SsForumPostTableid, SsForumPost, SsForumForum
from forum.verify import AddThreadVerify


class ThreadView(APIView):
    def post(self, request):
        verify = AddThreadVerify(data=request.data)
        verify.is_valid()
        fid = verify.data.get('fid')
        subject = verify.data.get('subject')
        message = verify.data.get('message')
        now = datetime.datetime.now(tz=pytz.utc)
        user = request.user
        thread = SsForumThread.objects.create(fid=fid, author=user.nick_name, authorid=user.id, subject=subject,
                                              lastposter=user.id, status=32, dateline=now, lastpost=now)
        post_table = SsForumPostTableid.objects.create()
        post = SsForumPost.objects.create(pid=post_table.pid, fid=fid, tid=thread.tid, first=1, author=user.nick_name,
                                          authorid=user.id, subject=subject, message=message, status=0, dateline=now)

        SsForumForum.objects.filter(fid=fid).update(posts=F('posts')+1, threads=F('threads')+1)

        data = {
            "tid": thread.tid,
            "pid": post.pid
        }

        return Response({"code": 0, "data": data})



