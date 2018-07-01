from django.conf.urls import include, url
from mainapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^marketing/(\S*)/$',views.marketing,name='marketing'),
]