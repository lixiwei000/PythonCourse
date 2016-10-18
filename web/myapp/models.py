from django.db import models
from django import forms
# Create your models here.

class UserInfo(models.Model):

    username = models.CharField(max_length=50,error_messages={'required':'用户名不能为空','invalid':'用户名非法'})

    password = models.CharField(max_length=100,error_messages={'required':"密码不能为空"})

    gender = models.IntegerField(default=1)

    createTime = models.DateTimeField(default= '2016-10-13 16:53:42')

    memo = models.CharField(max_length=2000)

    userType = models.ForeignKey('UserType')



class UserType(models.Model):

    typeNme = models.CharField(max_length=20,default='')

class UserGroup(models.Model):

    groupName = models.CharField(max_length=20)

    userInfo = models.ManyToManyField('UserInfo')

class Args(models.Model):

    name = models.CharField(max_length=100,null=False)

    remark = models.CharField(max_length=100,null=True)

    createTime = models.DateTimeField(auto_now_add=True)

    updateTime = models.DateTimeField(auto_now=True)

    genderChoices = (
        (u'1', u'Male'),
        (u'2', u'Female'),
        (u'3', u'Gay')
    )

    gender = models.CharField(max_length=2,choices=genderChoices)

class RegisterForm(forms.Form):

    username = forms.CharField(max_length=100)

    email = forms.EmailField(max_length=100,required=True,error_messages={'invalid':"别乱填邮箱好吗".encode(encoding='utf8')})