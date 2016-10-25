
from django.conf.urls import url
from bbs.views import *
from web import settings

urlpatterns = [
    url(r'^index/',index),
]
