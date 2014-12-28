#coding=utf8
'''
Created on 2014年7月18日

@author: Derek Xie

user_id/dept:JNK/checi/time/lat/lng/
'''
from django.db import models
from utils.base import BaseModelManager
from django.contrib import admin

class UdpMapManager(BaseModelManager):
    pass

class UdpMap(models.Model):
    class Meta:
        verbose_name_plural = u'UDP返回的地图数据'

    user_id = models.CharField(max_length=30)
    dept = models.CharField(max_length=20)
    checi = models.CharField(max_length=20)
    time = models.CharField(max_length=50)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)

    object = UdpMapManager()

    def __str__(self):
        return self.user_id

class UdpMapAdmin(admin.ModelAdmin):
    list_display = ('user_id','checi','time')

admin.site.register(UdpMap, UdpMapAdmin)