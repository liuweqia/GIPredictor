from django.conf.urls import patterns, url

from gip import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index')

)