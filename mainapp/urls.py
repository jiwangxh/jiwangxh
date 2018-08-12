from django.conf.urls import include, url
from mainapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^marketing/(\S*)/$',views.marketing,name='marketing'),
    url(r'^culture/$',views.culture,name='culture'),
    url(r'^production/$', views.production,name='production'),
    url(r'^mineclearnce/$', views.mineclearnce,name='mineclearnce'),
    url(r'joinus/$', views.joinus,name="joinus"),
]