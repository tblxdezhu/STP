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
from pyecharts import Bar, Line
from celery.task.control import revoke
from celery import chain, signature
from celery.app import control
import datetime
import pickle
from .google_earth_related import data_process, get_all_kmls

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
    for area in task.area:
        run_slam.delay(str(area), str(request.user), task.id, queue="queue_env1")

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
    if request.POST.get('getkml') == "getkml":
        data, center_data = data_process(task.output_path)
        print(list(center_data.keys()))
        kmls_data = []
        for k in get_all_kmls(task.output_path):
            for key in sorted(data[k].keys()):
                kmls_data.append(data[k][key])
        return render(request, 'submitted.html', {'task': task, 'branchs': eval(task.branch), 'center_data': str(center_data[list(center_data.keys())[0]]).rstrip(","), 'kmls_data': kmls_data})
    return render(request, 'submitted.html', {'task': task, 'branchs': eval(task.branch), 'center_data': "{lat: 41.876, lng: -87.624}", })


def _get_task_kml(request, task_id):
    task = Task.objects.get(id=task_id)
    print(task.output_path)
    data, center_data = data_process(task.output_path)
    print(list(center_data.keys()))
    kmls_data = []
    for k in get_all_kmls(task.output_path):
        for key in sorted(data[k].keys()):
            kmls_data.append(data[k][key])
    content = {
        'task': task,
        'branchs': eval(task.branch),
        'center_data': center_data[list(center_data.keys())[0]],
        'kmls_data': kmls_data
    }
    for kml_data in kmls_data:
        print(kml_data)
    print(center_data[list(center_data.keys())[0]])
    lat = ""
    lng = ""
    # eval(center_data[list(center_data.keys())[0]])
    line = line_test()
    myechart1 = line.render_embed()
    script_list = line.get_js_dependencies()
    return render(request, 'submitted.html', {'task': task,
                                              'branchs': eval(task.branch),
                                              'center_data': "hahahahah",
                                              'kmls_data': kmls_data, 'myechart2': myechart1, 'script_list': script_list})


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
    bar = bar_test()
    line = line_test()
    myechart = bar.render_embed()
    myechart1 = line.render_embed()
    script_list = bar.get_js_dependencies()
    script_list.append(line.get_js_dependencies())
    return render(request, 'dashboard.html', {'tasks': tasks, 'my_tasks': my_tasks, 'if_dashboard_active': 'active', 'myechart': myechart, 'myechart1': myechart1, 'script_list': script_list})


@login_required
def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'all_tasks.html', {'tasks': tasks})


@login_required
def all_my_tasks(request):
    tasks = Task.objects.filter(tester=request.user)
    return render(request, 'all_my_tasks.html', {'tasks': tasks})


def bar_test():
    attr = ["1", "2", "3", "4", "5", "6"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("test")
    bar.add("A", attr, v1, is_stack=True)
    bar.add("B", attr, v2, is_stack=True, is_toolbox_show=False)
    return bar


def line_test():
    attr = ["1", "2", "3", "4", "5", "6"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    line = Line("test")
    line.add("A", attr, v1, mark_point=["average"])
    line.add("B", attr, v2, is_smooth=True, mark_line=["max", "average"], is_toolbox_show=False)
    return line
