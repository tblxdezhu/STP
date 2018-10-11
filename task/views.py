from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Task
from task.tasks import print_task, run
from django.core.urlresolvers import reverse

import math

from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D
from celery.task.control import revoke

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


# Create your views here.
@login_required
def test(request):
    return render(request, 'run_slam_ssa_test.html', {'if_test_active': 'active'})


@login_required
def submitted(request):
    branchs = {'common': request.POST['common'], 'algo_common': request.POST['algo_common'], 'algo_vehicle_offlineslam': request.POST['algo_vehicle_offlineslam'],
               'common-sam': request.POST['common-sam'], 'algo_common-sam': request.POST['algo_common-sam']}
    task = Task(tester=request.user, mode=request.POST['select_mode'], branch=branchs, area=request.POST.getlist('check_box_list'))
    task.save()
    # result = print_task.delay("xu")
    # print(result.task_id)
    celery_task = run.delay("memmingen", str(request.user))

    # while True:
    #     print(result.status)
    #     if result.ready():
    #         break
    # print(result.status)
    # return render(request, 'submitted.html', {'task': task})
    return HttpResponseRedirect(reverse('task_id', kwargs={'task_id': task.id}))


@login_required
def task_process(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.POST.get('stoptask', None):
        revoke(task.celery_id, terminate=True)
    return render(request, 'submitted.html', {'task': task, 'branchs': eval(task.branch)})


@login_required
def dashboard(request):
    tasks = Task.objects.all()[0:5]
    my_tasks = Task.objects.filter(tester=request.user)[0:5]
    l3d = line3d()
    myechart = l3d.render_embed()
    script_list = l3d.get_js_dependencies()
    return render(request, 'dashboard.html', {'tasks': tasks, 'my_tasks': my_tasks, 'if_dashboard_active': 'active', 'myechart': myechart, 'script_list': script_list})


@login_required
def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'all_tasks.html', {'tasks': tasks})


@login_required
def all_my_tasks(request):
    tasks = Task.objects.filter(tester=request.user)
    return render(request, 'all_my_tasks.html', {'tasks': tasks})


def line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("Demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True,
               visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return line3d
