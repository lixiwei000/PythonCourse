from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Advertise.Hello Django")


def list(request, name,id):
    print(name,id)
    return HttpResponse('Advertise. %s , %s' % (name,id))
