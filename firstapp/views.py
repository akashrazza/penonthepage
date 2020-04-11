from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.db.models import Max
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def index(request):
    aaa=models.firstapp.objects.all().order_by('-date')
    obj=aaa.order_by('-views')[0:3:]
    paginator=Paginator(aaa,3)
    page=request.GET.get('page')
    try:
        post=paginator.get_page(page)
    except PageNotAnInteger:
        post=Paginator.page(1)
    except TypeError:
        post = Paginator.page(1)
    except EmptyPage:
        post=Paginator.page(Paginator.num_pages)


    return render(request,'index.html',{'name':post,'obj':obj})
def mostPOpular():
    obj=models.firstapp.objects.all().order_by('-views')
    obj=obj[0:3:]
    return obj

def add(request,a):
    #num1=request.GET['num1']
    #num2=request.GET['num2']
    #result=int(num1)+int(num2)
    result=a
    return render(request,'result.html',{'result':result})

def single(request,a):
    obj1=mostPOpular()
    obj=models.firstapp.objects.get(id=a)
    obj.views=obj.views+1
    obj.save()
    comm=models.comment.objects.filter(post_id=a)
    return render(request,'single.html',{'obj': obj,'comm':comm,'obj1':obj1})

def comment(request,a):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']

    comm=models.comment(post_id_id=a,name=name,comment=message)
    comm.save()
    ret=single(request,a)
    return ret
def indexReq(request,a):
    obj=None
    if(a=='2'):
        a='Technology'
        obj=models.firstapp.objects.filter(category=a)
    elif(a=='1'):
        a = 'Poetry'
        obj = models.firstapp.objects.filter(category=a)
    elif(a=='3'):
        a = 'Politics'
        obj = models.firstapp.objects.filter(category=a)
    elif(a=='4'):
        a = 'photography'
        obj = models.firstapp.objects.filter(category=a)
    if(obj == None):
        return HttpResponse("nothing found")
    return render(request,'index.html',{'name':obj})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')