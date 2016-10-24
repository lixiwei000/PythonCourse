# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='userGroup',
        ),
        migrations.AddField(
            model_name='usergroup',
            name='userInfo',
            field=models.ManyToManyField(to='myapp.UserInfo'),
        ),
    ]