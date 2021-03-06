#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 18:44
# @Author  : Zhenxuan Xu
# @File    : Device_settings.py.py
# @Software: Pycharm professional
"""
Django settings for STP2 project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery

djcelery.setup_loader()
BROKER_URL = 'amqp://stp:test1234@stp-server:5672//'
CELERY_RESULT_BACKEND = 'amqp://stp:test1234@stp-server:5672//'
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_ACKS_LATE = True
CELERY_ACCEPT_CONTENT = ['pickle']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '%)7gzyzhx2g%ylpag=+!n@b6b--sx4hwsla5b874tea@f&vxxo'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webserver',
    'task',
    'djcelery',
    'data',
    'lab',
    'results',
)

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'STP2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'STP2.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stp',
        'USER': 'stpadmin',
        'PASSWORD': 'test1234',
        'HOST': '10.69.142.12',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'test/'),
)

