#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/30 3:11 PM
# @Author  : Zhenxuan Xu
# @File    : tasks.py
# @Software: Pycharm professional

from celery import task
import time
from django_celery_results.models import TaskResult
import os


@task
def print_task(name):
    print("hello {}".format(name))
    time.sleep(30)
    os.system("touch ~/this_is_django_celery_test.txt")
    print("task over")


@task
def testtask2():
    print("this is task2 ************")
