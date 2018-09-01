#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.


#Content Management table start
class ContentManage(models.Model):
    pass

#Page Management table start
class PageManage(models.Model):
    pass




#-------------------------------------------------------------------------------------------------

#Global Titles tables
class GlobalTitle(models.Model):
    gt_id=models.IntegerField(primary_key=True)
    gt_name=models.CharField(max_length=10,unique=True)
    gt_logo=models.ImageField(upload_to='globaltitle',default="/static/media/globaltitle/logo.icon")
    gt_content=models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s' %self.gt_name
    class Meta:
        db_table='globaltitle'

#Global Advert tables
class GlobalAdvert(models.Model):
    ga_id=models.IntegerField(primary_key=True)
    ga_name=models.CharField(max_length=10,unique=True)
    ga_images=models.ImageField(upload_to='globaladvert',default='')
    ga_content=models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s' %self.ga_name
    class Meta:
        db_table='globaladvert'



#Global Management table start
class GlobalManage(models.Model):
    gm_globaltitle=models.ForeignKey(GlobalTitle)
    gm_globaladvert=models.ForeignKey(GlobalAdvert)


#--------------------------------------------------------------------------------------------------





#Home Page PhotoLbum start-----------------------------------------------------------------------
class PhotoLbum(models.Model):
    pl_id=models.IntegerField(primary_key=True)
    pl_name=models.CharField(max_length=10,unique=True)
    pl_title=models.CharField(max_length=100)
    pl_images=models.ImageField(upload_to='photolbum')
    def __unicode__(self):
        return u'%s' %self.pl_name
    class Meta:
        db_table='photolbum'

#Home Page Marketing start
class Marketing(models.Model):
    mt_id=models.IntegerField(primary_key=True)
    mt_name=models.CharField(max_length=10,unique=True)
    mt_title=models.CharField(max_length=20)
    mt_content=models.TextField(default="Nothing there Nothing there Nothing there Nothing there Nothing there Nothing there")
    mt_icon=models.ImageField(upload_to='marketing',default='')
    mt_images=models.ImageField(upload_to='marketing',default='')
    def __unicode__(self):
        return u'%s' %self.mt_name
    class Meta:
        db_table='marketing'

#Home Page Featurette start
class Featurette(models.Model):
    ft_id=models.IntegerField(primary_key=True)
    ft_name=models.CharField(max_length=10,unique=True)
    ft_title=models.CharField(max_length=20)
    ft_content=models.TextField(default="Nothing there Nothing there Nothing there Nothing there Nothing there Nothing there")
    ft_images=models.ImageField(upload_to='featurette')
    def __unicode__(self):
        return u'%s' %self.ft_name
    class Meta:
        db_table='featurette'

#-*-----------------------------------------------------------------------------------------------



#Home Page Content table start
class HomePageContent(models.Model):
    hc_title=models.ForeignKey(GlobalTitle)
    hc_advert=models.ForeignKey(GlobalAdvert)
    hc_photolbum=models.ForeignKey(PhotoLbum)
    hc_marketing=models.ForeignKey(Marketing)
    hc_featurette=models.ForeignKey(Featurette)





#------------------------------------------------------------
#Culture Timeline table start
class Timeline(models.Model):
    tl_id=models.IntegerField(primary_key=True)
    tl_name=models.CharField(max_length=100,unique=True)
    tl_headertitle=models.CharField(max_length=100,default='Surprising Headline Right Here')
    tl_releasetime=models.CharField(max_length=20,default='3 hours ago')
    tl_content=models.CharField(max_length=1000,default='Lorem Ipsum and such.')

    def __unicode__(self):
        return u'%s'%self.tl_name

#----------------------------------------------------------------
#Production Data tables start
class Production(models.Model):
    p_id=models.IntegerField(primary_key=True)
    p_name=models.CharField(max_length=20,unique=True)
    p_subject=models.CharField(max_length=30,default='Headder')
    p_introduce=models.TextField()
    p_images=models.p_images=models.ImageField(upload_to='production')
    p_link=models.CharField(max_length='300',default='')

    def __unicode__(self):
        return u'%s' %self.p_name

    class Mate:
        db_table='production'

#------------------------------------------------------------------
#Joinus Data table start
class JoinusData(models.Model):
    jd_name = models.CharField(max_length=10, default='')
    jd_phone = models.CharField(max_length=20, default='')
    jd_professional = models.CharField(max_length=100, default='')
    jd_interest = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return u'%s'%self.jd_name

    class Meta:
        db_table='joinusdata'
