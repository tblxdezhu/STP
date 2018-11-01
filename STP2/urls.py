"""STP2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from webserver import views
from task.views import dashboard, all_tasks, all_my_tasks, _get_dashboard_status

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login),
    url(r'^dashboard/', dashboard),
    url(r'^alltasks/', all_tasks),
    url(r'^allmytasks/', all_my_tasks),
    url(r'^data/', include('data.urls')),
    url(r'^test/', include('task.urls', app_name='task', namespace='test')),
    url(r'^machine/', include('lab.urls')),
    url(r'^coming/', views.coming),
]
