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
from .run_offlineSLAM import Vehicle, Run
import logging
from .SLAM_config import *
import subprocess
import pickle
from .models import Task
import datetime
from .compile_code import Compile_code


@task
def get_branch():
    repo_list = ['common', 'algorithm_common', 'algorithm_vehicle_offlineslam', 'algorithm_sam']
    code_path = "/home/roaddb/source/core"
    for repo in repo_list:
        os.chdir(os.path.join(code_path, repo))
        print(repo)
        status, output = subprocess.getstatusoutput("git branch -a")
        print(output)


@task
def run_slam(area, tester, task_id, queue):
    task = Task.objects.get(id=task_id)
    task.status = "SLAM"
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    vehicle = Vehicle(area, tester)
    task.output_path = os.path.join(output_path, tester, area, str(task_id), date, vehicle.mode)
    task.save()

    subtask_id_list = []
    for rtv in vehicle.rtvs:
        imu = rtv.replace('.rtv', '.imu')
        case_output_path = os.path.join(task.output_path, os.path.basename(rtv).strip('.rtv'))
        if imu in vehicle.imus:
            single_task = single_run_slam.apply_async(args=[rtv, imu, slam_config, camera_config, case_output_path], queue=queue)
            print(single_task.task_id)
            subtask_id_list.append(single_task.task_id)

    celery_task = Task.objects.get(id=task_id)
    celery_task.celery_id = subtask_id_list
    celery_task.save()
    return vehicle.output_path


@task
def print_task(name):
    print("hello {}".format(name))
    time.sleep(30)
    os.system("touch ~/this_is_django_celery_test.txt")
    print("task over")


@task
def run(area, tester, mode="SLAM"):
    vehicle = Vehicle(area, mode, tester)
    vehicle.vehicle_slam()
    # with open("test.pkl", 'wb') as f:
    #     print("save pkl")
    #     pickle.dump(vehicle, f)
    return vehicle.output_path


@task
def single_run_slam(rtv, imu, slam_config_file, camera_file, case_output_path):
    os.makedirs(case_output_path)
    logging.info("mkdir {}".format(case_output_path))
    run_cmd_list = [vehicle_exec, '--rtv', rtv, '--iimu', imu, '--ip', slam_config_file, '--ic', camera_file]
    os.chdir(case_output_path)
    run_cmd = ' '.join(run_cmd_list)
    logging.info(run_cmd)
    # Run.execute_cmd(run_cmd)
    # status, output = subprocess.getstatusoutput(run_cmd)
    subprocess.getstatusoutput(run_cmd)
    # print("running SLAM {}".format(rtv))
    # subprocess.call(['/Users/test1/PycharmProjects/github/STP/test.sh {}'.format(rtv)], shell=True)
    # print("{} run over".format(rtv))


@task
def test_celery(rtv):
    print("running SLAM {}".format(rtv))
    subprocess.call(['/Users/test1/PycharmProjects/github/STP/test.sh'], shell=True)
    print("{} run over".format(rtv))


@task
def test_ssa(output_path):
    print("running SSA : path:{}".format(output_path))
    subprocess.call(['/Users/test1/PycharmProjects/github/STP/ssa.sh'], shell=True)
    print("SSA run over")


@task
def build(branchs):
    print(branchs)
    compile_code = Compile_code(branchs)
    compile_code.run_compile("10.69.142.16")
