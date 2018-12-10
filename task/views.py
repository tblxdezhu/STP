from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Task
from results.models import Results
from task.tasks import single_run_slam, test_celery, test_ssa, run, print_task, run_slam, get_branch, build, backup, work_flow
from .run_offlineSLAM import Vehicle
from django.core.urlresolvers import reverse
from .SLAM_config import *
import math
import os
from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar, Line, Grid, configure

configure(global_theme='walden')
from celery.task.control import revoke
from celery import chain, signature
from celery.app import control
import datetime
import pickle
from .google_earth_related import data_process, get_all_kmls
import subprocess
import json
import csv
import time

# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
#
# schduler = BackgroundScheduler()
# schduler.add_jobstore(DjangoJobStore(), "default")

# def test_job(task_id):
#     time.sleep(4)
#     print("i am a test job {}".format(task_id))
#
#
# def test_1_job():
#     time.sleep(4)
#     print("i am a test 1st job")
#
#
# register_events(schduler)

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@login_required
def test(request):
    get_branch()
    # Test schduler
    # try:
    #     schduler.add_job(func=test_1_job, next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=3))
    #     schduler.start()
    #     print("Scheduler started!")
    # except Exception:
    #     pass

    return render(request, 'run_slam_ssa_test.html', {'if_test_active': 'active'})


@login_required
def submitted(request):
    branchs = {
        'common': request.POST['common'],
        'algorithm_common': request.POST['algorithm_common'],
        'algorithm_vehicle_offlineslam': request.POST['algorithm_vehicle_offlineslam'],
        'common_sam': request.POST['common_sam'],
        'algorithm_common_sam': request.POST['algorithm_common_sam'],
        'algorithm_sam': request.POST['algorithm_sam'],
        'vehicle': request.POST['vehicle']
    }
    task = Task(tester=request.user, mode=request.POST['select_mode'], branch=branchs, area=request.POST.getlist('check_box_list'), status="Waiting", description=request.POST['description'])
    task.save()
    task.output_path = os.path.join(output_path, str(task.id))
    task.save()
    if_build = True
    if request.POST.get('ifskipbuild') == 'skipbuild':
        if_build = False
    work_flow.apply_async(args=[if_build, task.id])
    # for area in task.area:
    #     work_flow.apply_async(args=[if_build, str(task.mode), str(area), task.id, branchs])
    # schduler.add_job(func=test_job, id=str(task.id), args=(task.id,), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=3),replace_existing=True)
    return HttpResponseRedirect(reverse('test:task_id', kwargs={'task_id': task.id}))


# @login_required
# def submitted(request):
#     branchs = {'common': request.POST['common'], 'algorithm_common': request.POST['algorithm_common'], 'algorithm_vehicle_offlineslam': request.POST['algorithm_vehicle_offlineslam'],
#                'common_sam': request.POST['common_sam'], 'algorithm_common_sam': request.POST['algorithm_common_sam'], 'algorithm_sam': request.POST['algorithm_sam'],
#                'vehicle': request.POST['vehicle']}
#     print("branchs", branchs)
#     print(request.POST.get('ifskipbuild'))
#     task = Task(tester=request.user, mode=request.POST['select_mode'], branch=branchs, area=request.POST.getlist('check_box_list'), status="Waiting")
#     task.save()
#     if task.id % 2 == 0:
#         queue = "env1"
#     else:
#         queue = "env1"
#     build_sam = False
#     if_build = True
#     # build.apply_async(args=[branchs, task.id, build_sam], queue=queue)
#     # for area in task.area:
#     #     print(area)
#     #     run_slam.apply_async(args=[str(area), str(request.user), task.id, queue], queue=queue)
#     # chain_result = chain(run.s("test", str(request.user), "SLAM"), test_ssa.s())()
#     try:
#         for area in task.area:
#             if request.POST.get('ifskipbuild') == 'skipbuild':
#                 if_build = False
#             chain_result = chain(build.s(branchs, task.id, if_build, build_sam).set(queue=queue), run_slam.s(str(area), str(request.user), task.id, queue).set(queue=queue),
#                                  backup.s(task.id).set(queue=queue))
#             chain_result()
#     except Exception as e:
#         print(e)
#     # backup.apply_async(args=[task.id], queue=queue)
#     # result = print_task.delay("xu")
#     # print(result.task_id)
#     # vehicle = Vehicle("test", str(request.user))
#     # celery_id_list = []
#     # for rtv in vehicle.rtvs:
#     #     imu = rtv.replace('.rtv', '.imu')
#     #     case_output_path = os.path.join(vehicle.output_path, vehicle.mode, os.path.basename(rtv).strip('.rtv'))
#     #     if imu in vehicle.imus:
#     #         single_task = single_run_slam.delay(rtv, imu, slam_config, camera_config, case_output_path)
#     #         print(single_task.task_id)
#     #         celery_id_list.append(single_task.task_id)
#     # celery_task = Task.objects.get(id=task.id)
#     # celery_task.celery_id = celery_id_list
#     # celery_task.save()
#
#     # *********************TEST SINGLE MODE OF SLAM*********************
#     # test_vehicle_rtvs = ['1.rtv', '2.rtv', '3.rtv', '4.rtv', '5.rtv']
#     # celery_id_list = []
#     # for rtv in test_vehicle_rtvs:
#     #     single_task = test_celery.delay(rtv)
#     #     print(single_task.task_id)
#     #     celery_id_list.append(single_task.task_id)
#     #
#     # ssa_task = test_ssa.delay()
#     # celery_id_list.append(ssa_task.task_id)
#     #
#     # celery_task = Task.objects.get(id=task.id)
#     # celery_task.celery_id = celery_id_list
#     # celery_task.save()
#     # ******************************OVER********************************
#
#     # celery_id_list = []
#
#     # chain_result = chain(run.s("test", str(request.user), "SLAM"), test_ssa.s())()
#     # print_task.delay("this is test rabbitmq")
#     # print_task.delay("this is test2 rabbitmq")
#     # print("test", chain_result.parent.task_id)
#     # print("test2", chain_result.task_id)
#     # celery_id_list.append(chain_result.parent.task_id)
#     # celery_id_list.append(chain_result.parent.parent.task_id)
#     # celery_slam_task = run.apply_async(args=["test", str(request.user), "SLAM"])
#     # celery_id_list.append(celery_slam_task.task_id)
#     # celery_ssa_task = test_ssa.delay()
#     # celery_id_list.append(celery_ssa_task.task_id)
#     # celery_id_list.extend([chain_result.parent.task_id, chain_result.task_id])
#     # celery_task = Task.objects.get(id=task.id)
#     # celery_task.celery_id = celery_id_list
#     # celery_task.save()
#
#     # while True:
#     #     print(result.status)
#     #     if result.ready():
#     #         break
#     # print(result.status)
#     # return render(request, 'submitted.html', {'task': task})
#     return HttpResponseRedirect(reverse('test:task_id', kwargs={'task_id': task.id}))


@login_required
def task_process(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.POST.get('stoptask') == "stop":
        print("stop the task:{}".format(task.celery_id))
        task.status = "STOP"
        task.save()
        try:
            revoke(eval(task.celery_id), terminate=True)
        except TypeError:
            print("stop the task")
    if request.POST.get('getkml') == "getkml":
        try:
            data, center_data = data_process(task.output_path)
        except TypeError:
            return render(request, 'submitted.html', {'task': task, 'branchs': eval(task.branch), 'center_data': "{lat: 41.876, lng: -87.624}", "nokmls": True})
        kmls_data = []
        for k in get_all_kmls(task.output_path):
            for key in sorted(data[k].keys()):
                kmls_data.append(data[k][key])
        return render(request, 'submitted.html', {'task': task, 'branchs': eval(task.branch), 'center_data': str(center_data[list(center_data.keys())[0]]).rstrip(","), 'kmls_data': kmls_data})
    attr = Results.objects.show_task_id()

    line = line_time_kf(attr)
    myechart1 = line.render_embed()
    script_list = line.get_js_dependencies()
    return render(request, 'submitted.html',
                  {'task': task, 'areas': eval(task.area), 'branchs': eval(task.branch), 'center_data': "{lat: 41.876, lng: -87.624}", 'myechart2': myechart1, 'script_list': script_list})


@login_required
def get_area_kml(request, task_id, area):
    print(task_id, area)
    task = Task.objects.get(id=task_id)
    data, center_data = data_process(task.output_path)
    return JsonResponse({'task_id': task_id, 'area': area})
    # return HttpResponse("{} {}".format(task_id, area))


def _get_task_kml(request, task_id, area):
    task = Task.objects.get(id=task_id)
    data, center_data = data_process(os.path.join(task.output_path, area))
    print("center_data", center_data)
    # return JsonResponse({'task_id': task_id, 'area': area, 'center_data': center_data[list(center_data.keys())[0]]},'kmls_data': kmls_data)

    print(list(center_data.keys()))
    kmls_data = []
    for k in get_all_kmls(os.path.join(task.output_path, area)):
        for key in sorted(data[k].keys()):
            kmls_data.append(data[k][key])
    content = {
        'task': task,
        'branchs': eval(task.branch),
        'center_data': center_data[list(center_data.keys())[0]],
        'kmls_data': kmls_data
    }
    # for kml_data in kmls_data:
    #     print(kml_data)
    # print(center_data[list(center_data.keys())[0]])
    lat = ""
    lng = ""
    # eval(center_data[list(center_data.keys())[0]])
    # attr = Results.objects.show_task_id()
    #
    # line = line_time_kf(attr)
    # myechart1 = line.render_embed()
    # script_list = line.get_js_dependencies()
    # return render(request, 'submitted.html', {'task': task,
    #                                           'branchs': eval(task.branch),
    #                                           'center_data': "hahahahah",
    #                                           'kmls_data': kmls_data, 'myechart2': myechart1, 'script_list': script_list})
    print("content", content)
    return JsonResponse(content)


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
    attr = Results.objects.show_task_id()
    script_list = []
    line = line_time_kf(attr)
    bar = bar_mp_kf(attr)
    # myechart = bar.render_embed()
    # myechart = line.render_embed()
    script_list.extend(line.get_js_dependencies())
    # script_list = bar.get_js_dependencies()
    script_list.extend(bar.get_js_dependencies())
    grid = Grid(width="auto")
    grid.add(line, grid_bottom="60%")
    grid.add(bar, grid_top="60%")
    myechart = grid.render_embed()
    script_list.extend(grid.get_js_dependencies())

    run_rtv_numbers = Results.objects.order_by('-id').values_list('id').first()[0]
    seconds = sum([int(i[0]) for i in Results.objects.values_list('time')])
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    time_cost = "%02dd:%02dh:%02dm:%02ds" % (d, h, m, s)

    return render(request, 'dashboard.html', {
        'run_rtv_numbers': run_rtv_numbers,
        'time_cost': time_cost,
        'tasks': tasks,
        'my_tasks': my_tasks,
        'if_dashboard_active': 'active',
        'myechart': myechart,
        'script_list': script_list
    })


@login_required
def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'all_tasks.html', {'tasks': tasks})


@login_required
def all_my_tasks(request):
    tasks = Task.objects.filter(tester=request.user)
    return render(request, 'all_my_tasks.html', {'tasks': tasks})


def bar_mp_kf(attr):
    total_mps = [Results.objects.total(task_id=t, keyword='mps') for t in attr]
    total_kfs = [Results.objects.total(task_id=t, keyword='kfs') for t in attr]
    value = [round(mps / total_kfs[total_mps.index(mps)], 4) for mps in total_mps]
    bar = Bar("MP/KF", title_top="50%")
    bar.add("", attr, value, is_datazoom_show=True, datazoom_xaxis_index=[0, 1], is_toolbox_show=False, xaxis_name="task id", xaxis_name_pos="end")
    return bar


def line_time_kf(attr):
    total_time = [Results.objects.total(task_id=t, keyword='time') for t in attr]
    total_kf = [Results.objects.total(task_id=t, keyword='kfs') for t in attr]
    value = [round(t / total_kf[total_time.index(t)], 4) for t in total_time]
    line = Line("Time/KF")
    line.add("", attr, value, is_datazoom_show=True, datazoom_xaxis_index=[0, 1], is_smooth=True, is_toolbox_show=False, xaxis_name="task id", yaxis_name="seconds", yaxis_name_gap="40",
             xaxis_name_pos="end")
    return line


def get_branch():
    repo_list = ['common', 'algorithm_common', 'algorithm_vehicle_offlineslam', 'algorithm_sam', 'vehicle']
    code_path = "/media/psf/Untitled/Auto_test_SLAM/envs/stp_envs/core"
    if not os.path.exists(code_path):
        code_path = "/data1/stp_resources/source/core"
    init_path = os.getcwd()
    json_data = {}
    for repo in repo_list:
        os.chdir(os.path.join(code_path, repo))
        status, output = subprocess.getstatusoutput("git branch -a")
        json_data[repo] = []
        for branch in output.split("\n"):
            if "remotes/core" in branch:
                json_data[repo].append(branch.split("remotes/core/")[1].strip())
            elif "remotes/origin" in branch:
                json_data[repo].append(branch.split("remotes/origin/")[1].strip())
            elif "*" in branch:
                json_data[repo].append(branch.split("*")[1].strip())
            else:
                json_data[repo].append(branch.strip())
    with open("{}/static/jsons/branchs.json".format(init_path), "w") as f:
        json.dump(json_data, f)
    os.chdir(init_path)


@login_required
def download_file(request, task_id):
    def file_iterator(file_name):
        try:
            with open(file_name, 'rb') as f:
                while True:
                    c = f.read()
                    if c:
                        yield c
                    else:
                        break
        except FileNotFoundError:
            print("file not found")

    file = "{}/static/data/alignmentkmls.zip".format(os.getcwd())

    response = StreamingHttpResponse(file_iterator(file_name=file))

    response['Content-Type'] = 'application/zip'
    response['Content-Disposition'] = 'attachment; filename="{}.zip"'.format(task_id)

    return response
