# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20161017_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(error_messages={'required': '密码不能为空'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(error_messages={'invalid': '用户名非法', 'required': '用户名不能为空'}, max_length=50),
        ),
    ]
