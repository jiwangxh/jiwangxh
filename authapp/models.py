from django.db import models

# Create your models here.



class UserInfo(models.Model):
    uname=models.CharField(max_length=40,unique=True)
    upassword=models.CharField(max_length=40)
    uemail=models.CharField(max_length=35,default=' ')
    uphone=models.CharField(max_length=11,default=' ')
    uaddress=models.CharField(max_length=100,default=' ')
    uicon=models.ImageField(upload_to='userinfo',default='/media/userinfo/one.png')

    def __unicode__(self):
        return u'%s' % self.uname
    class Meta:
        db_table = 'userinfo'

class Role(models.Model):
    rid = models.IntegerField(primary_key=True)
    rname =models.CharField(max_length=20)
    user=models.ForeignKey(UserInfo)
    def __unicode__(self):
        return u'%s' % self.rname
    class Meta:
        db_table = 'role'

