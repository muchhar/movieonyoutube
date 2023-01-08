from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from django.db import close_old_connections
def index(request):
    close_old_connections()
    #collecting action movie
    actionm= movielist.objects.filter(movie_home="1")[:6]#1
    actionm.til="Action"
    #collecting horror movie
    horrorm= movielist.objects.filter(movie_home="2")[:6]#2
    horrorm.til="Horror"
    #collecting comedy movie
    comedym= movielist.objects.filter(movie_home="3")[:6]#3
    comedym.til="Comedy"
    #collecting scifi movie
    scifim= movielist.objects.filter(movie_home="4")[:6]#4
    scifim.til="Sci-Fi"
    a=[actionm,horrorm,comedym,scifim]
    return render(request,'usersite/index.html',{'a':a})
def catone(request,fd):
    
    dis=movielist.objects.filter(movie_cat=fd)
    a=[dis]
    man=fd
    msg=""
    if len(dis)==0:
        msg="404! Data Not Found"
        man="Error"
    else:
        pass
    
    
    return render(request,'usersite/catpage.html',{'a':a,'msg':msg,'man':man})
def lanone(request,fd2):
    dis=movielist.objects.filter(movie_lang=fd2)
    a=[dis]
    man=""
    msg=""
    if len(dis)==0:
        msg="404! Data Not Found"
        man="Error"
    else:
        man=fd2.title()
    return render(request,'usersite/lanpage.html',{'a':a,'msg':msg,'man':man})
def privacy(request):
    return render(request,'usersite/privacy.html')