from django.shortcuts import render
from mainapp.models import *

# Create your views here.

def index(request):

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
        # photolbum star
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
    # TimeLine make data start
    timelineone = Timeline.objects.filter(fl_id=1)
    timelinetwo = Timeline.objects.filter(fl_id=2)
    timelineothree = Timeline.objects.filter(fl_id=3)
    timelinefour = Timeline.objects.filter(fl_id=4)
    timelinefive = Timeline.objects.filter(fl_id=5)
    timelinesix = Timeline.objects.filter(fl_id=6)
    timelineseven = Timeline.objects.filter(fl_id=7)
    timelineeight = Timeline.objects.filter(fl_id=8)

    context = {
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



def production(request):
    return render(request,'mainapp/production.html')

def mineclearnce(request):
    return render(request,'mainapp/mineclearance.html')



#------joinus-------
def joinus(request):
    return render(request,'mainapp/joinus.html')
