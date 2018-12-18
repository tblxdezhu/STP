#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 14:26
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional

from django.conf.urls import include, url
from results import views

urlpatterns = [
    url(r'^$', views.analyse_data),
    url(r'^get_json_data/', views.get_json_data)
]
