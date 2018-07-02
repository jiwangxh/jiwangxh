#-*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from hashlib import sha1
from authapp.models import *


# Create your views here.

def register(request):
    return render(request,'authapp/register.html')

def register_handle(request):
    #Receiving user input
    post=request.POST
    uname=post.get('user_name')
    upassword=post.get('password')
    upassword2=post.get('cpassword')
    #To determine whether the password is the same or not
    if upassword !=  upassword2:
        return redirect('/register/')
    #Password encryption
    s1=sha1()
    s1.update(upassword)
    upassword3=s1.hexdigest()
    #Create an objects
    user=UserInfo()
    user.uname=uname
    user.upassword=upassword3
    user.save()
    #Registration success,got to the login page
    return redirect('/login/')

def register_exist(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})


def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'authapp/login.html',context)

def login_handle(request):
    #Receiving requests information
    post=request.POST
    uname=post.get('user_name')
    upassword=post.get('password')
    jizhu=post.get('jizhu',0)

    #reason username query objects
    users=UserInfo.objects.filter(uname=uname)
    #judge:If the user name is not found, if it is checked, the password is correct.
    if len(users)==1:
        s1=sha1()
        s1.update(upassword)
        if s1.hexdigest() == users[0].upassword:
            red = HttpResponseRedirect('/userinfo/')
            #Remember the name of the username
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context={'title':'用户登录','error_name':0,'error_pwd':1, 'uname':uname,'upassword':upassword}
            return render(request, 'authapp/login.html',context)
    else:
        context={'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upassword':upassword}
        return render(request,'authapp/login.html',context)

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')


def userinfo(request):
    user=UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post=request.POST
        user.uemail=post.get('email')
        user.uphone=post.get('phone')
        user.uaddress=post.get('address')
        user.uicon=post.get('icon')
        user.save()
    context={
        'title':'用户中心','user':user
    }
    return render(request,'authapp/userinfo.html',context)


def retrieve(request):
    pass

def modify(request):
    pass
