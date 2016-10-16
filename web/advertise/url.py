from django.conf.urls import url
from advertise.views import *

urlpatterns = [
    # url映射 ------ 函数
    url(r'^index/', index),
    url(r'^list/(?P<name>\S*)/(?P<id>\d*)', list,{'id':"000"})
    # url映射 ------- 文件

]