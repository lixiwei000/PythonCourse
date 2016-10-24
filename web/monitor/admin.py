from django.contrib import admin

# Register your models here.
from monitor import models

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("username",'password','email','createTime','userType')
    search_fields = ('username','email')
    list_filter = ('username','email')
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('groupName',)
    search_fields = ('groupName',)
    list_filter =  ('groupName',)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('typeName',)
    search_fields = ('typeName',)
    list_filter = ('typeName',)
admin.site.register(models.UserInfo,UserInfoAdmin)
admin.site.register(models.UserGroup,UserGroupAdmin)
admin.site.register(models.UserType,UserTypeAdmin)