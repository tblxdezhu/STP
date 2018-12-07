#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 3:29 PM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional
from django.conf.urls import include, url
from task import views

app_name = "task"

urlpatterns = [
    url(r'^$', views.test),
    url(r'^submitted$', views.submitted),
    url(r'^(?P<task_id>[0-9]{1,5})/$', views.task_process, name='task_id'),
    url(r'^(?P<task_id>[0-9]{1,5})/status$', views._get_task_status),
    url(r'^(?P<task_id>[0-9]{1,5})/download$', views.download_file, name='download'),
    url(r'^(?P<task_id>[0-9]{1,5})/(?P<area>[\s\S]*)/$', views.get_area_kml),

]
