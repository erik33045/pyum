from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('app.urls')),
                       url(r'^pyum/', include('app.urls')),
                       url(r'^app/', include('app.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
