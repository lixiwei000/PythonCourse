from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from monitor.common import tryInt
from monitor.models import *
from monitor.forms import *
from monitor.htmlHelper import *
import math
import json
# Create your views here.

def login(request):
    ret = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if all([username,password]):
            result = UserInfo.objects.filter(username=username,password=password).count()
            print(username,password,result)
            if result == 1:
                return redirect("/monitor/index/")
            else:
                ret['status'] = "用户名或密码错误"
        else:
            ret['status'] = "用户名或密码不能为空"
    return render_to_response("monitor/login.html")

def register(request):
    ret = {}
    typeList = UserType.objects.all()
    groupList = UserGroup.objects.all()
    userList = UserInfo.objects.all()
    if request.method == 'GET':
        ret['typeList'] = typeList
        ret['groupList'] = groupList
        ret['userList'] = UserInfo.objects.all()
        for user in userList:
            if user.userGroup is not None:
                for group in user.userGroup.all():
                    print(group.groupName)
    else:
        # Form
        username = request.POST.get("username")
        password = request.POST.get("password")
        userType = request.POST.get("userType")
        userGroup = request.POST.get("userGroup")
        # Find UserInfo
        userRes = UserInfo.objects.filter(username = username,userType = userType,userGroup=userGroup)
        if userRes.count() >= 1:
            ret['status'] = "该用户已经创建过"
        else:
            # Create UserInfo
            userType = UserType.objects.get(id = userType)
            userGroup = UserGroup.objects.get(id = userGroup)
            userInfo = UserInfo.objects.create(username=username,password=password,userType=userType)
            # UserGroup.objects.create(userInfo=userInfo,userGroup=userGroup)
            # userGroup.userinfo_set.add(userInfo)
            userInfo.userGroup.add(userGroup)
            # userInfo.usergroup_set.add(userGroup)
            ret['status'] = "创建成功"
            ret['userList'] = UserInfo.objects.all()
            ret['typeList'] = typeList
            ret['groupList'] = groupList
    return render_to_response("monitor/register.html",ret)

def formRegister(request):

    user = User()
    errorObj = None
    firstErrorMsg = ''
    if request.method == "POST":
        user = User(request.POST)
        validRes = user.is_valid()
        if validRes:
            pass
        else:
            # print(user.errors)
            errorObj = user.errors
            firstErrorMsg = list(user.errors.as_data().values())[0][0]
            print(firstErrorMsg)
    return render_to_response("monitor/formRegister.html",{"data":user,"errors":errorObj,"firstErrorMsg":firstErrorMsg})

def ajax(request):

    if (request.method == 'POST'):
        print(request.POST)
        data = {'status':'OK','msg':'后台接收到了请求','data':[1,2,3,4,5]}
        return HttpResponse(json.dumps(data))

    return render_to_response("monitor/ajax.html")

def search(request):
    res = {}
    typeList = UserType.objects.all()
    groupList = UserGroup.objects.all()
    userList = UserInfo.objects.all()
    res['typeList'] = typeList
    res['groupList'] = groupList
    res['userList'] = userList
    if request.method == "POST":
        type = request.POST.get("userType",None)
        group = request.POST.get("userGroup",None)
        params = {}
        if type != "all":
            params['userType__id'] = type
        if group != "all":
            params['userGroup__id'] = group
        userList = UserInfo.objects.filter(**params)
        res['userList'] = userList
        for user in userList:
            print(user)
    return render_to_response("monitor/search.html", res)



def index(request):
    return HttpResponse("主页面")

def list(request):
    pageSize = int(request.COOKIES.get("pageSize",5))
    userList = UserInfo.objects.all()
    count = userList.count()
    page = tryInt(request.GET.get("page",1),1)
    currentPage = tryInt(page,1)

    pageInfo = PageInfo(currentPage,count,pageSize)
    pageString = pager(currentPage,pageInfo.totalPage)

    ret = {'userList':userList[pageInfo.start:pageInfo.end],'total':count,'currentPage':currentPage,'totalPage':pageInfo.totalPage,'pageHtml':pageString}
    response = render_to_response("monitor/list.html",ret)
    response.set_cookie("pageSize",pageSize,path="/monitor")
    return response