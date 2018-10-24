#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 3:08 PM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional

from django.conf.urls import include, url
from lab import views

urlpatterns = [
    url(r'^$', views.lab_info),
    url(r'^lab_cpu$', views.lab_cpu),
    url(r'^lab_memory$', views.lab_used_memory),
    url(r'^lab_cpu_memory$', views.lab_cpu_memory),
]
