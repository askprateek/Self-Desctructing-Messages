from django.shortcuts import render
from django.http import HttpResponse
from .models import Secret
# Create your views here.

def index(request):
    a = Secret.objects.all()
    a=a[0]
    text = str(a.slug) +"<br> "+ str(a.message) +" <br>"+ str( a.status)
    return HttpResponse(text)

def match(request,slug):
    obj =Secret.objects.get(slug=slug)
    if obj.status==0:
        obj.status=1
        obj.save()
        return HttpResponse(obj.message)
    else:
        return HttpResponse('Msg has been destructed')
