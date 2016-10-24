from django.db import models
from django.forms import forms
from time import time
# Create your models here.
class UserType(models.Model):

    typeName = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "用户类型表"

class UserInfo(models.Model):

    username = models.CharField(max_length=50,error_messages={'required':'用户名不能为空','invalid':'用户名格式不正确'})

    password = models.CharField(max_length=100,error_messages={'required':'密码不能为空'})

    email = models.CharField(max_length=100,null=True,error_messages={'required':'邮箱不能为空','invalid':'邮箱格式不正确'})

    createTime = models.DateTimeField(default= '2016-10-13 16:53:42')

    userType = models.ForeignKey('UserType')

    userGroup = models.ManyToManyField('UserGroup')

    class Meta:
        verbose_name_plural = "用户信息表"
    # def __str__(self):
    #     return "username = %s password = %s email = %s createTime = %s userType = %s userGroup = %s" % (self.username, self.password, self.email, self.createTime.strftime("%Y-%m-%d %H:%M:%S"), self.userType.typeName, ' '.join([ group.groupName for group in self.userGroup.all()]))

class UserGroup(models.Model):

    groupName = models.CharField(max_length=200,null=True)

    class Meta:
        verbose_name_plural = "用户组信息表"

class Asset(models.Model):

    hostName = models.CharField(max_length=100,null=True)

    ip = models.GenericIPAddressField(default="0.0.0.0")

    groupId = models.ForeignKey("UserGroup")



