from django.conf.urls import include, url
from authapp import views


urlpatterns = [
    url(r'^register',views.register,name='register'),
]