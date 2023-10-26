from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,"demo/index.html")

def greet(request,name):
    return render(request,"demo/greet.html",{'name':len(name)%2==0})