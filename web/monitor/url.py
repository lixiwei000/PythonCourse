from django.conf.urls import url
from monitor import views
urlpatterns = [
    url(r'^login',views.login),
    url(r'^formRegister',views.formRegister),
    url(r'^register',views.register),
    url(r'^search',views.search),
    url(r'^ajax',views.ajax),
    url(r'^list',views.list),
]