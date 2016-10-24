from decorator import decorate
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
def doFilter(beforeFunc,afterFunc):
    def checkLogin(func):
        def wrapper(request,*args,**kwargs):
            beforeFunc()
            print("C")
            loginDict = request.session.get('login')
            if loginDict:
                username = loginDict['username']
                if username:
                    print(username)
                    return func(request,*args,**kwargs)
                else:
                    return render_to_response("shop/login.html",{"status":"请重新登录"})
            else:
                return render_to_response("shop/login.html",{"status":"请先登录"})
            # afterFunc()
        print("B")
        return wrapper
    print("A")
    return checkLogin


def before():
    print("Before Function...")

def after():
    print("After Function...")

def login(request):
    errors = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "admin":
            request.session['login'] = {'username':username}
            return redirect("/shop/index/")
        else:
            errors['status'] = "用户名或密码错误"
    else:
        errors['status'] = "请先登陆"
    return render_to_response("shop/login.html",errors)

@doFilter(before,after)
def index(request):
    print("index")
    # userDict = request.session.get('login')
    # if userDict:
    #     username = userDict['username']
    return render_to_response("shop/index.html")
    # else:
    # return redirect("/shop/login/")
