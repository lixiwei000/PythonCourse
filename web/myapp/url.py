from django.conf.urls import url
from myapp.views import *

urlpatterns = [
    # url映射 ------ 函数
    url(r'^index/', index),
    url(r'^list/(?P<name>\S*)/(?P<id>\d*)/', list,{'id':"000"}),
    url(r'^add/(?P<name>\S*)/',add),
    url(r'^delete/(?P<id>\d*)/',delete),
    url(r'^update/(?P<id>\d*)/(?P<name>\w*)/',update),
    url(r'^updateList/(?P<id>\d*)/(?P<remark>\w*)/',updateList),
    url(r'^get/(?P<name>\w*)/',get),
    url(r'^getWithLimit/(?P<limit>\d*)/',getWithLimit),
    url(r'^login/',login),
    url(r'^register/',register)
    # url映射 ------- 文件

]