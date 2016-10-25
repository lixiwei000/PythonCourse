from django.db import models

# Create your models here.

class UserType(models.Model):

    display = models.CharField(max_length=100)

    def __unicode__(self):
        return self.display

class Admin(models.Model):

    username = models.CharField(max_length=100)

    password = models.CharField(max_length=100)

    email = models.EmailField()

    userType = models.ForeignKey("UserType")

    def __unicode__(self):
        return self.username

class Chat(models.Model):

    content = models.TextField()

    user = models.ForeignKey("Admin")

    createDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content

class News(models.Model):

    title = models.CharField(max_length=100)

    summary = models.CharField(max_length=256)

    url = models.URLField()

    favorCount = models.IntegerField(default=0)

    replayCount = models.IntegerField(default=0)

    newsType = models.ForeignKey("NewsType")

    user = models.ForeignKey("Admin")

    createDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class NewsType(models.Model):

    display = models.CharField(max_length=100)

    def __unicode__(self):
        return self.display

class Reply(models.Model):

    content = models.TextField()

    user = models.ForeignKey("Admin")

    new = models.ForeignKey("News")

    createDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content