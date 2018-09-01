# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from mainapp.models import *

# Create your views here.

def index(request):

    #GlobalTitle make data start
    title=GlobalTitle.objects.filter(gt_name="index")

    # photolbum make data start
    photolbumone = PhotoLbum.objects.filter(pl_id=1)
    photolbumtwo = PhotoLbum.objects.filter(pl_id=2)
    photolbumthree = PhotoLbum.objects.filter(pl_id=3)
    photolbumfour = PhotoLbum.objects.filter(pl_id=4)
    #photolbum make data stop

    #marketing make data start
    marketingone=Marketing.objects.filter(mt_id=1)
    marketingtwo=Marketing.objects.filter(mt_id=2)
    marketingthree=Marketing.objects.filter(mt_id=3)
    #marketing make data stop

    #featurette make data start
    featuretteone=Featurette.objects.filter(ft_id=1)
    featurettetwo=Featurette.objects.filter(ft_id=2)
    featurettethree=Featurette.objects.filter(ft_id=3)
    #featurette make data stop

    user=request.session

    centext = {

        #globaltitle start
        'title': title,

        # photolbum start
        'photolbumone': photolbumone,
        'photolbumtwo': photolbumtwo,
        'photolbumthree': photolbumthree,
        'photolbumfour': photolbumfour,

        #marketing start
        'marketingone': marketingone,
        'marketingtwo': marketingtwo,
        'marketingthree': marketingthree,

        #meaturette start
        'featuretteone': featuretteone,
        'featurettetwo': featurettetwo,
        'featurettethree': featurettethree,


    }
    return render(request, 'mainapp/index.html', centext)


def marketing(request,marketingname):
    marketing=Marketing.objects.filter(mt_name=marketingname)
    centext={
        'marketing':marketing,
    }

    return render(request, 'mainapp/marketing.html',centext)


#----Community culture
def culture(request):

    #GlobalTitle make data start
    title = GlobalTitle.objects.filter(gt_name="index")

    # TimeLine make data start
    timelineone = Timeline.objects.filter(tl_id=1)
    timelinetwo = Timeline.objects.filter(tl_id=2)
    timelineothree = Timeline.objects.filter(tl_id=3)
    timelinefour = Timeline.objects.filter(tl_id=4)
    timelinefive = Timeline.objects.filter(tl_id=5)
    timelinesix = Timeline.objects.filter(tl_id=6)
    timelineseven = Timeline.objects.filter(tl_id=7)
    timelineeight = Timeline.objects.filter(tl_id=8)

    context = {

        #title start
        'title':title,

        'timelineone': timelineone,
        'timelinetwo': timelinetwo,
        'timelineothree': timelineothree,
        'timelinefour': timelinefour,
        'timelinefive': timelinefive,
        'timelinesix': timelinesix,
        'timelineseven': timelineseven,
        'timelineeight': timelineeight,
    }
    return render(request,'mainapp/culture.html',context)


#---------------
def production(request):

    # GlobalTitle make data start
    title = GlobalTitle.objects.filter(gt_name="index")

    #Production make data start
    production=Production.objects.all()

    context = {
        #title start
        'title':title,

        #production stat
        'production':production,
    }

    return render(request,'mainapp/production.html',context)

def mineclearnce(request):
    return render(request,'mainapp/mineclearance.html')



#-------------
def joinus(request):


    # GlobalTitle make data
    title = GlobalTitle.objects.filter(gt_name="index")


    context = {
        # title start
        'title': title,
    }


    return render(request,'mainapp/joinus.html',context)


def joinus_headle(request):

    post = request.POST
    fname = post.get("fullname")
    fphone = post.get("phonenumber")
    fprofessional = post.get("professional")
    finterest = post.get("interest")

    # 向数据库库写写数据
    joinusdata = JoinusData()
    joinusdata.jd_name = fname
    joinusdata.jd_phone = fphone
    joinusdata.jd_professional = fprofessional
    joinusdata.jd_interest = finterest
    joinusdata.save()


    return render(request,'mainapp/Informationsubmission.html')

