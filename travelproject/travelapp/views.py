from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Guide

# Create your views here.





def demo(request):
    obj=Place.objects.all()
    Gui=Guide.objects.all()
    return render(request,'index.html',{'result':obj,'guide':Gui})
#def addition(request):
    #x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
   # r1=x+y
    #r2=x-y
    #r3=x*y
    #r4=x/y
    #return render(request,'result.html',{'res1':r1,'res2':r2,'res3':r3,'res4':r4})