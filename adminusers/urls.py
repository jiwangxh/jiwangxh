from django.conf.urls import url,include
from adminusers import  views

# app_name ='adminusers'
urlpatterns = [
    url(r'^register/',views.register, name='register'),
    url(r'^userinfo/',views.userinfo, name='userinfo'),
]