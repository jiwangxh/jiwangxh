from django.shortcuts import render
from authapp.models import *

# Create your views here.

def register(request):
    return render(request,'authapp/register.html')



def login(request):
    pass

def retrieve(request):
    pass

def modify(request):
    pass
