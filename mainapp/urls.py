from django.conf.urls import include, url
from mainapp import views


urlpatterns = [
    url(r'^index/',views.index, name='index')
]