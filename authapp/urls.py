from django.conf.urls import include, url
from authapp import views


urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_exist/$',views.register_exist),

    url(r'^login/$',views.login,name='login'),
    url(r'^login_handle/$',views.login_handle),

    url(r'^userinfo/$',views.userinfo,name='userinfo'),

    url(r'^logout/$',views.logout,name='logout'),

]
