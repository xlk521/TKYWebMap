#coding=utf-8
'''
Created on 2014年4月15日

@author: Derek Xie
'''
from django.db import models
from django.contrib.auth.models import BaseUserManager

class BaseModelManager(BaseUserManager, models.Manager):
    #django.contrib.auth.models.BaseUserManager
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None