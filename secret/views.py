from django.shortcuts import render
from django.http import HttpResponse
from .models import Secret
# Create your views here.

def index(request):
    a = Secret.objects.all()
    a=a[0]
    text = str(a.slug) +"<br> "+ str(a.message) +" <br>"+ str( a.status)
    return HttpResponse(text)

def match(request):
    return 0
