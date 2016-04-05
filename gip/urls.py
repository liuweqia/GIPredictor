from django.conf.urls import patterns, url

from gip import views

urlpatterns = patterns('',
        url(r'^$', views.category, name='category'),
        url(r'^about/$', views.about, name='about'),


)