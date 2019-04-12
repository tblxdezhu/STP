from __future__ import unicode_literals

import grequests

# from gevent import monkey;monkey.patch_socket()
# import gevent
# import socket

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Task
from results.models import Results
from task.tasks import build, work_flow
from .run_offlineSLAM import Vehicle
from django.core.urlresolvers import reverse
from .SLAM_config import *
import math
import os
from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar, Line, Grid, configure, Page, Pie, Timeline, Geo, Map
# configure(global_theme='walden')
from django.shortcuts import render_to_response
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
from webserver.models import Data, Machine
from random import randint
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor
from multiprocessing import Pool
from functools import wraps

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


def page_not_found(request):
    return render(request, '404.html')


def timefunc(func):
    @wraps(func)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("@timefunc:{} took {} seconds".format(func.__name__, str(t2 - t1)))
        return result

    return measure_time


@login_required
def test(request):
    # get_branch(request)
    # areas = Data.objects.all_areas()
    areas = Data.objects.all()
    return render(request, 'run_slam_ssa_test.html', {'if_test_active': 'active', 'areas': areas, 'branches': get_branch()})


@login_required
def submitted(request):
    print(request.user)
    if str(request.user) == 'guest':
        return render(request, "404.html")
    # branchs = {
    #     'common': request.POST['common'],
    #     'algorithm_common': request.POST['algorithm_common'],
    #     'algorithm_common_slam':request.POST['algorithm_common_slam'],
    #     'algorithm_vehicle_offlineslam': request.POST['algorithm_vehicle_offlineslam'],
    #     'common_sam': request.POST['common_sam'],
    #     'algorithm_common_sam': request.POST['algorithm_common_sam'],
    #     'algorithm_sam': request.POST['algorithm_sam'],
    #     'vehicle': request.POST['vehicle']
    # }
    branchs = {
        'common': request.POST['common'],
        'algorithm_common': request.POST['algorithm_common'],
        'algorithm_common_slam': request.POST['algorithm_common_slam'],
        'algorithm_vehicle_offlineslam': request.POST['algorithm_vehicle_offlineslam'],
        'vehicle': request.POST['vehicle']
    }
    print(branchs)

    # task = Task(tester=request.user, mode=request.POST['select_mode'], branch=branchs, area=request.POST.getlist('select_list'), status="Waiting", description=request.POST['description'])
    # task.save()
    task = Task.objects.create(tester=request.user, mode=request.POST['select_mode'], branch=branchs, area=request.POST.getlist('select_list'), status="Waiting",
                               description=request.POST['description'], machine_id='0000')
    print("new task id:", id(task))
    if_build = True
    if request.POST.get('ifskipbuild') == 'skipbuild':
        if_build = False

    print("if_build:", if_build)
    print("task_id:", task.id)
    work_flow.apply_async(args=[if_build, task.id])
    return HttpResponseRedirect(reverse('test:task_id', kwargs={'task_id': task.id}))


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

    def __str2dic(str_):
        output_dic = {}
        str_ = str_.split(",")
        output_dic[str_[0].split(":")[0].lstrip("{")] = float(str_[0].split(":")[1])
        output_dic[str_[1].split(":")[0].lstrip()] = float(str_[1].split(":")[1].rstrip("}"))
        return output_dic

    center_data = {}
    kmls_data = []
    if not task.status == 'build':
        try:
            for area in eval(task.area):
                data, center, kmls = data_process(os.path.join(task.output_path, area), task_id)
                for k in kmls:
                    for key in sorted(data[k].keys()):
                        kmls_data.append(data[k][key])
                center_data[area] = __str2dic(center[list(center.keys())[0]])
        except Exception as e:
            print("data process", e)
            pass

    task.center = center_data
    task.save(update_fields=['center'])

    page = draw_line(task_id)
    myechart = page.render_embed()
    script_list = page.get_js_dependencies()
    try:
        task_ip = Machine.objects.get(machine_id=task.machine_id).ip
    # 'No machine online, your task has been added to the task list.'
    except Exception as e:
        return render(request, '404.html', {'error_info': e})
    return render(request, 'submitted.html',
                  {'task': task, 'areas': eval(task.area), 'branchs': eval(task.branch), 'center_data': "{lat: 41.876, lng: -87.624}", 'myechart': myechart, 'script_list': script_list,
                   'kmls_data': kmls_data, 'task_ip': task_ip})


def get_kmls_data(request, task_id):
    task = Task.objects.get(id=task_id)
    center_data = {}
    kmls_data = []

    def __str2dic(str_):
        output_dic = {}
        str_ = str_.split(",")
        output_dic[str_[0].split(":")[0].lstrip("{")] = float(str_[0].split(":")[1])
        output_dic[str_[1].split(":")[0].lstrip()] = float(str_[1].split(":")[1].rstrip("}"))
        return output_dic

    for area in eval(task.area):
        data, center, kmls = data_process(os.path.join(task.output_path, area), task_id)
        for k in kmls:
            for key in sorted(data[k].keys()):
                kmls_data.append(data[k][key])
        center_data[area] = __str2dic(center[list(center.keys())[0]])
    task.center = center_data
    task.save()
    # print(kmls_data)
    map_jquery_txt = """
    <script>
                    function get_result(area) {
                        $.getJSON('/test/214/' + area, function (ret) {
                            center_data = {lat: parseFloat(ret.center_data['lat']), lng: parseFloat(ret.center_data['lng'])};
                            map.setCenter(center_data);
                        })
                    }
                    var map;

                    function initMap() {
                        map = new google.maps.Map(document.getElementById('map'), {
                            center: {lat: 41.876, lng: -87.624},
                            zoom: 13,
                            mapTypeId: google.maps.MapTypeId.SATELLITE
                        });
                        
                    
    """
    insert_txt = ''.join(kmls_data)
    end_txt = """
    }
    </script>
    """
    print(map_jquery_txt + insert_txt + end_txt)
    return HttpResponse(map_jquery_txt + insert_txt + end_txt)


def draw_line(task_id):
    page = Page()
    task = Task.objects.get(id=task_id)
    data_to_show = ['mp_kf', 'time', 'weak_rate', 'kfs', 'mps', 'slam_len']
    for area in eval(task.area):
        line = Line(area)
        line.width = 'auto'
        attr = Results.objects.show_data_of_area(task_id=task_id, keyword="rtv_name", area=str(area))
        for data in data_to_show:
            value = Results.objects.show_data_of_area(task_id=task_id, keyword=data, area=area)
            line.add(str(data), attr, value, is_smooth=True, is_datazoom_show=True, datazoom_range=[20, 100], is_more_utils=True)
        page.add(line)
    return page


@login_required
def get_area_kml(request, task_id, area):
    print(task_id, area)
    task = Task.objects.get(id=task_id)
    data, center_data = data_process(task.output_path)
    return JsonResponse({'task_id': task_id, 'area': area})


def _get_task_kml(request, task_id, area):
    task = Task.objects.get(id=task_id)
    return JsonResponse({
        'area': area,
        'center_data': eval(task.center)[area]
    })


# def get_task_status(celery_id):
#     task = test_celery.AsyncResult(celery_id)
#     return task.state

def _get_task_status(request, task_id):
    # def __get_celery_task_status(celery_task_id):
    #     celery_task = run.AsyncResult(celery_task_id)
    #     return celery_task.state

    task = Task.objects.get(id=task_id)
    status = {}
    # print("celery_id:", task.celery_id)
    # status['SLAM'] = run_slam.AsyncResult(eval(task.celery_id)[0]).state
    # status['SSA'] = run_slam.AsyncResult(eval(task.celery_id)[1]).state
    status['status'] = task.status
    status['mode'] = task.mode
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

    # run_rtv_numbers = Results.objects.order_by('-id').values_list('id').first()[0]
    # seconds = sum([int(i[0]) for i in Results.objects.values_list('time')])
    # m, s = divmod(seconds, 60)
    # h, m = divmod(m, 60)
    # d, h = divmod(h, 24)
    # time_cost = "%02dd:%02dh:%02dm:%02ds" % (d, h, m, s)

    return render(request, 'dashboard.html', {
        # 'run_rtv_numbers': run_rtv_numbers,
        # 'time_cost': time_cost,
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
             xaxis_name_pos="end", datazoom_range=[80, 100])
    return line


#
# def get_repo_branch(repo):
#     start = time.time()
#     repo_branches = []
#     url = "https://stash.ygomi.com:7990/rest/api/1.0/projects/RC/repos/{}/branches?limit=100".format(repo)
#     a = HTTPBasicAuth('zhenxuan.xu', 'YGomi258')
#     req = requests.get(url=url, auth=a)
#     for branch in req.json()['values']:
#         repo_branches.append(branch['displayId'])
#     end = time.time()
#     return repo + ",over"

@timefunc
def get_branch():
    repo_list = ['common', 'algorithm_common', 'algorithm_common_slam', 'algorithm_vehicle_offlineslam', 'algorithm_sam', 'vehicle']
    a = HTTPBasicAuth('zhenxuan.xu', 'YGomi258')
    branches = {}
    for repo in repo_list:
        branches[repo] = []
        url = "https://stash.ygomi.com:7990/rest/api/1.0/projects/RC/repos/{}/branches?limit=100".format(repo)
        req = requests.get(url=url, auth=a)
        for branch in req.json()['values']:
            branches[repo].append(branch['displayId'])


    # urls = ["https://stash.ygomi.com:7990/rest/api/1.0/projects/RC/repos/{}/branches?limit=100".format(repo) for repo in repo_list]
    # rs = (grequests.get(url=u, auth=a) for u in urls)
    # responses = grequests.map(rs, size=3)
    #
    return branches
    # return JsonResponse(branches)
    # get branches info from local
    # repo_list = ['common', 'algorithm_common', 'algorithm_vehicle_offlineslam', 'algorithm_sam', 'vehicle']
    # code_path = "/media/psf/Untitled/Auto_test_SLAM/envs/stp_envs/core"
    # if not os.path.exists(code_path):
    #     code_path = "/data1/stp_resources/source/core"
    # init_path = os.getcwd()
    # json_data = {}
    # for repo in repo_list:
    #     os.chdir(os.path.join(code_path, repo))
    #     status, output = subprocess.getstatusoutput("git branch -a")
    #     json_data[repo] = []
    #     for branch in output.split("\n"):
    #         if "remotes/core" in branch:
    #             json_data[repo].append(branch.split("remotes/core/")[1].strip())
    #         elif "remotes/origin" in branch:
    #             json_data[repo].append(branch.split("remotes/origin/")[1].strip())
    #         elif "*" in branch:
    #             json_data[repo].append(branch.split("*")[1].strip())
    #         else:
    #             json_data[repo].append(branch.strip())
    # with open("{}/static/jsons/branchs.json".format(init_path), "w") as f:
    #     json.dump(json_data, f)
    # os.chdir(init_path)


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

    # def zipDir(dirpath, outFullName):
    #     """
    #     压缩指定文件夹
    #     :param dirpath: 目标文件夹路径
    #     :param outFullName: 压缩文件保存路径+xxxx.zip
    #     :return: 无
    #     """
    #     zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    #     for path, dirnames, filenames in os.walk(dirpath):
    #         # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
    #         fpath = path.replace(dirpath, '')
    #
    #         for filename in filenames:
    #             zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    #     zip.close()

    file = "{}/static/data/alignmentkmls.zip".format(os.getcwd())

    response = StreamingHttpResponse(file_iterator(file_name=file))

    response['Content-Type'] = 'application/zip'
    response['Content-Disposition'] = 'attachment; filename="{}.zip"'.format(task_id)

    return response
