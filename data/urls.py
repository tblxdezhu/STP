#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 1:13 PM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional

from django.conf.urls import include, url
from data import views

urlpatterns = [
    url(r'^large$', views.large_data),
    url(r'^mini$', views.mini_data),
    url(r'^error$', views.error_data)
]
