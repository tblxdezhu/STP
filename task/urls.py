#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 3:29 PM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional
from django.conf.urls import include, url
from task import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^submitted$', views.submitted),
    url(r'^(?P<task_id>[0-9]{1,5})/$', views.task_process, name='task_id'),

]
