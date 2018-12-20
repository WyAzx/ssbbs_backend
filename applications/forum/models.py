import time

from django.db import models


class SsForumThread(models.Model):
    tid = models.AutoField(primary_key=True)
    fid = models.PositiveIntegerField(default=0)
    posttableid = models.PositiveSmallIntegerField(default=0)
    typeid = models.PositiveSmallIntegerField(default=0)
    sortid = models.PositiveSmallIntegerField(default=0)
    readperm = models.PositiveIntegerField(default=0)
    price = models.SmallIntegerField(default=0)
    author = models.CharField(max_length=15)
    authorid = models.CharField(max_length=36)
    subject = models.CharField(max_length=80)
    dateline = models.DateTimeField()
    lastpost = models.DateTimeField()
    lastposter = models.CharField(max_length=36)
    views = models.PositiveIntegerField(default=0)
    replies = models.PositiveIntegerField(default=0)
    displayorder = models.IntegerField(default=0)
    highlight = models.IntegerField(default=0)
    digest = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    special = models.IntegerField(default=0)
    attachment = models.IntegerField(default=0)
    moderated = models.IntegerField(default=0)
    closed = models.PositiveIntegerField(default=0)
    stickreply = models.PositiveIntegerField(default=0)
    recommends = models.SmallIntegerField(default=0)
    recommend_add = models.SmallIntegerField(default=0)
    recommend_sub = models.SmallIntegerField(default=0)
    heats = models.PositiveIntegerField(default=0)
    status = models.PositiveSmallIntegerField(default=0)
    isgroup = models.IntegerField(default=0)
    favtimes = models.IntegerField(default=0)
    sharetimes = models.IntegerField(default=0)
    stamp = models.IntegerField(default=-1)
    icon = models.IntegerField(default=-1)
    pushedaid = models.IntegerField(default=0)
    cover = models.SmallIntegerField(default=0)
    replycredit = models.SmallIntegerField(default=0)
    relatebytag = models.CharField(max_length=255)
    maxposition = models.PositiveIntegerField(default=0)
    bgcolor = models.CharField(max_length=8)
    comments = models.PositiveIntegerField(default=0)
    hidden = models.PositiveSmallIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'ss_forum_thread'


class SsForumPost(models.Model):
    pid = models.PositiveIntegerField(unique=True)
    fid = models.PositiveIntegerField()
    tid = models.PositiveIntegerField(primary_key=True)
    first = models.IntegerField()
    author = models.CharField(max_length=15)
    authorid = models.CharField(max_length=36)
    subject = models.CharField(max_length=80)
    dateline = models.DateTimeField()
    message = models.TextField()
    useip = models.CharField(max_length=15)
    port = models.PositiveSmallIntegerField(default=0)
    invisible = models.IntegerField(default=0)
    anonymous = models.IntegerField(default=0)
    usesig = models.IntegerField(default=0)
    htmlon = models.IntegerField(default=0)
    bbcodeoff = models.IntegerField(default=0)
    smileyoff = models.IntegerField(default=0)
    parseurloff = models.IntegerField(default=0)
    attachment = models.IntegerField(default=0)
    rate = models.SmallIntegerField(default=0)
    ratetimes = models.PositiveIntegerField(default=0)
    status = models.IntegerField(default=0)
    tags = models.CharField(max_length=255)
    comment = models.IntegerField(default=0)
    replycredit = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'ss_forum_post'
        unique_together = (('tid', 'position'),)


class SsForumForum(models.Model):
    fid = models.AutoField(primary_key=True)
    fup = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    displayorder = models.SmallIntegerField(default=0)
    styleid = models.PositiveSmallIntegerField(default=0)
    threads = models.PositiveIntegerField(default=0)
    posts = models.PositiveIntegerField(default=0)
    todayposts = models.PositiveIntegerField(default=0)
    yesterdayposts = models.PositiveIntegerField(default=0)
    rank = models.PositiveSmallIntegerField(default=0)
    oldrank = models.PositiveSmallIntegerField(default=0)
    lastpost = models.CharField(max_length=110)
    domain = models.CharField(max_length=15)
    allowsmilies = models.IntegerField(default=0)
    allowhtml = models.IntegerField(default=0)
    allowbbcode = models.IntegerField(default=0)
    allowimgcode = models.IntegerField(default=0)
    allowmediacode = models.IntegerField(default=0)
    allowanonymous = models.IntegerField(default=0)
    allowpostspecial = models.PositiveSmallIntegerField(default=0)
    allowspecialonly = models.PositiveIntegerField(default=0)
    allowappend = models.PositiveIntegerField(default=0)
    alloweditrules = models.IntegerField(default=1)
    allowfeed = models.IntegerField(default=0)
    allowside = models.IntegerField(default=0)
    recyclebin = models.IntegerField(default=0)
    modnewposts = models.IntegerField(default=0)
    jammer = models.IntegerField(default=0)
    disablewatermark = models.IntegerField(default=0)
    inheritedmod = models.IntegerField(default=0)
    autoclose = models.SmallIntegerField(default=0)
    forumcolumns = models.PositiveIntegerField(default=0)
    catforumcolumns = models.PositiveIntegerField(default=0)
    threadcaches = models.IntegerField(default=0)
    alloweditpost = models.PositiveIntegerField(default=0)
    simple = models.PositiveIntegerField(default=0)
    modworks = models.PositiveIntegerField(default=0)
    allowglobalstick = models.IntegerField(default=0)
    level = models.SmallIntegerField(default=0)
    commoncredits = models.PositiveIntegerField(default=0)
    archive = models.IntegerField(default=0)
    recommend = models.PositiveSmallIntegerField(default=0)
    favtimes = models.PositiveIntegerField(default=0)
    sharetimes = models.PositiveIntegerField(default=0)
    disablethumb = models.IntegerField(default=0)
    disablecollect = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'ss_forum_forum'


class SsForumPostTableid(models.Model):
    pid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ss_forum_post_tableid'


# Create your models here.
