from django.conf.urls import patterns, url
from django.contrib import admin

from app import views


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'), )
