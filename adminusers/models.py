from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname=models.CharField(max_length=50, blank=True)
    uemail = models.CharField(max_length=35, blank=True)
    uphone = models.CharField(max_length=11, blank=True)
    uaddress = models.CharField(max_length=100, blank=True)
    uicon = models.ImageField(upload_to='userinfo', blank=True)

    class User(AbstractUser.Meta):
        pass