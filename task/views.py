from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Task
from task.tasks import single_run_slam, test_celery, test_ssa, run, print_task, run_slam
from .run_offlineSLAM import Vehicle
from django.core.urlresolvers import reverse
from .SLAM_config import *
import math
import os
from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D
from celery.task.control import revoke
from celery import chain, signature
from celery.app import control
import datetime
import pickle

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


# Create your views here.
@login_required
def test(request):
    return render(request, 'run_slam_ssa_test.html', {'if_test_active': 'active'})


@login_required
def submitted(request):
    branchs = {'common': request.POST['common'], 'algo_common': request.POST['algo_common'], 'algo_vehicle_offlineslam': request.POST['algo_vehicle_offlineslam'],
               'common-sam': request.POST['common-sam'], 'algo_common-sam': request.POST['algo_common-sam']}
    task = Task(tester=request.user, mode=request.POST['select_mode'], branch=branchs, area=request.POST.getlist('check_box_list'), status="Waiting")
    task.save()
    run_slam.delay("milford", str(request.user), task.id)

    # result = print_task.delay("xu")
    # print(result.task_id)
    # vehicle = Vehicle("test", str(request.user))
    # celery_id_list = []
    # for rtv in vehicle.rtvs:
    #     imu = rtv.replace('.rtv', '.imu')
    #     case_output_path = os.path.join(vehicle.output_path, vehicle.mode, os.path.basename(rtv).strip('.rtv'))
    #     if imu in vehicle.imus:
    #         single_task = single_run_slam.delay(rtv, imu, slam_config, camera_config, case_output_path)
    #         print(single_task.task_id)
    #         celery_id_list.append(single_task.task_id)
    # celery_task = Task.objects.get(id=task.id)
    # celery_task.celery_id = celery_id_list
    # celery_task.save()

    # *********************TEST SINGLE MODE OF SLAM*********************
    # test_vehicle_rtvs = ['1.rtv', '2.rtv', '3.rtv', '4.rtv', '5.rtv']
    # celery_id_list = []
    # for rtv in test_vehicle_rtvs:
    #     single_task = test_celery.delay(rtv)
    #     print(single_task.task_id)
    #     celery_id_list.append(single_task.task_id)
    #
    # ssa_task = test_ssa.delay()
    # celery_id_list.append(ssa_task.task_id)
    #
    # celery_task = Task.objects.get(id=task.id)
    # celery_task.celery_id = celery_id_list
    # celery_task.save()
    # ******************************OVER********************************

    # celery_id_list = []

    # chain_result = chain(run.s("test", str(request.user), "SLAM"), test_ssa.s())()
    # print_task.delay("this is test rabbitmq")
    # print_task.delay("this is test2 rabbitmq")
    # print("test", chain_result.parent.task_id)
    # print("test2", chain_result.task_id)
    # celery_id_list.append(chain_result.parent.task_id)
    # celery_id_list.append(chain_result.parent.parent.task_id)
    # celery_slam_task = run.apply_async(args=["test", str(request.user), "SLAM"])
    # celery_id_list.append(celery_slam_task.task_id)
    # celery_ssa_task = test_ssa.delay()
    # celery_id_list.append(celery_ssa_task.task_id)
    # celery_id_list.extend([chain_result.parent.task_id, chain_result.task_id])
    # celery_task = Task.objects.get(id=task.id)
    # celery_task.celery_id = celery_id_list
    # celery_task.save()

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
    if request.POST.get('stoptask') == "stop":
        print("stop the task:{}".format(task.celery_id))
        task.status = "STOP"
        task.save()
        revoke(eval(task.celery_id), terminate=True)
    return render(request, 'submitted.html', {'task': task, 'branchs': eval(task.branch)})


# def get_task_status(celery_id):
#     task = test_celery.AsyncResult(celery_id)
#     return task.state

def _get_task_status(request, task_id):
    def __get_celery_task_status(celery_task_id):
        celery_task = run.AsyncResult(celery_task_id)
        return celery_task.state

    task = Task.objects.get(id=task_id)
    status = {}
    print("celery_id:", task.celery_id)
    # status['SLAM'] = run_slam.AsyncResult(eval(task.celery_id)[0]).state
    # status['SSA'] = run_slam.AsyncResult(eval(task.celery_id)[1]).state
    status['status'] = task.status
    print(status)
    return JsonResponse(status)


def _get_dashboard_status(request):
    tasks = Task.objects.all()[0:5]
    my_tasks = Task.objects.filter(tester=request.user)[0:5]
    dashboard_status = {"all": {}, "mytasks": {}}
    for task in tasks:
        dashboard_status["all"][task.id] = task.status
    for my_task in my_tasks:
        dashboard_status["mytasks"][my_task] = my_task.status
    return JsonResponse(dashboard_status)


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
