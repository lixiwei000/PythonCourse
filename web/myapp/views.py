from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from myapp.models import Args, UserInfo,RegisterForm


def index(request):
    return HttpResponse("Myapp.Hello Django")


def list(request, name, id):
    print(name, id)
    return HttpResponse('Myapp. %s , %s' % (name, id))


def add(request, name):
    Args.objects.create(name=name, gender='M')
    return HttpResponse("OK")


def delete(request, id):
    Args.objects.get(id=id).delete()
    return HttpResponse("Delete OK")

def update(request,id,name):
    obj = Args.objects.get(id=id)
    obj.name = name
    obj.save()
    return HttpResponse("Update OK")

def updateList(request,id,remark):
    Args.objects.filter(id__gt = id).update(remark="批量更新")
    return HttpResponse("批量更新OK")

def get(request,name):
    objs = Args.objects.filter(name__contains=name)
    # print(objs)
    return HttpResponse([x.name for x in objs])

def getWithLimit(request,limit):
    allObjs = Args.objects.all().order_by('-id')
    limitObjs = allObjs[:int(limit)]#.values('id','name')
    print(limitObjs.query)
    return render_to_response("list.html",{'user':limitObjs})

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username",None)
        password = request.POST.get('password',None )
        result = UserInfo.objects.filter(username=username,password=password).count()
        if result == 1:
            return HttpResponse("登陆成功")
        else:
            return render_to_response("login.html",{"status":"用户名或密码错误"})
    else:
        return render_to_response("login.html")

def register(request):
    resForm = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            # print(form.errors.as_json())
            data = form.errors.as_data()
            print(data['email'][0].messages[0])
    return render_to_response("register.html",{"form":resForm})