#coding=utf8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('map.views',
    url(r'^$','map',name='map'),
)