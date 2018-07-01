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
    gt_logo=models.ImageField(default='null',upload_to='globaltitle')
    gt_content=models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s' %self.mt_name
    class Meta:
        db_table='globaltitle'

#Global Advert tables
class GlobalAdvert(models.Model):
    ga_id=models.IntegerField(primary_key=True)
    ga_name=models.CharField(max_length=10,unique=True)
    ga_images=models.ImageField(default='null',upload_to='globaladvert')
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
    mt_icon=models.ImageField(upload_to='marketing')
    mt_images=models.ImageField(upload_to='marketing')
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


