from django.conf.urls import patterns, url
from django.contrib import admin

from app import views


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^register/$', views.register, name='register'),
                       url(r'^search_recipes/$', views.search_recipes, name='search_recipes'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^home/$', views.home, name='home'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve'), )
