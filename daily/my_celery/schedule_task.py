#!/usr/bin/env python
# -*- coding: utf-8 -*-
from celery import Celery

app = Celery('schedule_task')
app.config_from_object('config') #以config.py作为配置文件导入参数

@app.task
def add(x,y):
    print x + y