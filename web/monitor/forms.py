from django import forms

class User(forms.Form):

    userName = forms.CharField(max_length=100,error_messages={'required':'用户名不能为空','invalid':'用户名格式错误'})

    password = forms.CharField(max_length=100,error_messages={'required':'密码不能为空','invalid':'密码格式错误'})

    email = forms.EmailField(required=True,error_messages={'required':'邮箱不能为空','invalid':'邮箱格式错误'})

    ip = forms.GenericIPAddressField(required=True,error_messages={'required':'IP不能为空','invalid':'IP地址格式错误'})