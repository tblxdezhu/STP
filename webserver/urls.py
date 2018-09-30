#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 2:45 PM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional
from webserver import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.login),
    
]
