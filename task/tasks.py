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
from .run_offlineSLAM import Vehicle, Run, Server
import logging
from .SLAM_config import *
import subprocess
import pickle
from .models import Task
import datetime
from .compile_code import Compile_code
from results.models import Results, Overview
from results.slam_quality import SlamQuality


def build(branchs, task_id, if_build=True, mode='slam', build_sam=False):
    if not mode == "slam":
        build_sam = True
    if if_build:
        print(branchs)
        task = Task.objects.get(id=task_id)
        task.status = 'build'
        task.save()
        branchs['is_sam'] = build_sam
        compile_code = Compile_code(branchs)
        try:
            compile_code.run_compile()
            task.status = 'builddone'
            task.save()
        except Exception as e:
            print(e)
            task.status = 'buildfailed'
            task.save()


@task
def work_flow(if_build, task_id):
    task = Task.objects.get(id=task_id)

    def __change_status(status):
        task.status = status
        # save() 方法会设定所有列的 值，而不是只设定 name 列的值。
        # 如果你所处的环境可能同时由其他操作修改其他列，最好只更新需要修改的值。
        # 为此，使用 QuerySet 对象的 update() 方法
        # TODO 需要将不必要的save替换为update
        task.save()
        logging.info("status change to {}".format(status))

    print(if_build, task.mode, task.area, task_id)
    # COMPILE THE CODE , DEFAULT MODE IS NOT BUILD ALGO_SAM
    build(eval(task.branch), task_id, if_build)

    for area in eval(task.area):
        vehicle = Vehicle(str(area), task.id)
        __change_status('SLAM')
        try:
            vehicle.vehicle_slam()
            __change_status('SLAMdone')
            try:
                task_result = SlamQuality(task_id, area).quality_to_dict()
                logging.info(task_result)
                for case_result in task_result[0][area]:
                    result = Results.objects.create(
                        task_id=task.id, area=area, mode='slam', rtv_name=case_result['RTV'], slam_len=case_result['SLAM_trajectory_length'], gps_len=case_result['GPS_trajectory_length'],
                        kfs=case_result['Total_number_of_KFs'], rtv_frames=case_result['Total_frames'], mps=case_result['Total_number_of_MPs'],
                        avg_track_len_mp=case_result['Average_track_length_of_MP'], weak_rate=case_result['Weak_convisibility_frame_rate'],
                        mp_kf=case_result['MP_per_KF'], time=case_result['Time'], efficiency=case_result['Efficiency']
                    )
            except Exception as e:
                logging.info("Parsing quality error as following, please operate the database manually:{}".format(e))
        except Exception as e:
            print(e)
            __change_status('SLAMfailed')

    if task.mode == 'SSA':
        build(eval(task.branch), task_id, if_build, task.mode)

        for area in eval(task.area):
            server = Server(str(area), task.id)
            __change_status('SSA')
            try:
                server.clean()
                server.rtv2gps()
                server.process()
                __change_status('SSAdone')
                __change_status('backup')
                try:
                    server.backup()
                except Exception as e:
                    print(e)
                    __change_status('backupfailed')
            except Exception as e:
                print(e)
                __change_status('SSAfailed')
        __change_status('done')


@task
def get_branch():
    repo_list = ['common', 'algorithm_common', 'algorithm_vehicle_offlineslam', 'algorithm_sam']
    for repo in repo_list:
        os.chdir(os.path.join(get_branchs_code_path, repo))
        print(repo)
        status, output = subprocess.getstatusoutput("git branch -a")
        print(output)


@task
def run_slam(build_status, area, tester, task_id, queue):
    if build_status == 0:
        print("build ok")
    task = Task.objects.get(id=task_id)
    task.status = "SLAM"
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    vehicle = Vehicle(area, tester)
    task.output_path = os.path.join(output_path, str(task_id), area, vehicle.mode)
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
    run_cmd_list = [vehicle_exec, '--rtv', rtv, '--iimu', imu, '--ip', slam_config_file, '--ic', camera_file, '--oqlt', os.path.join(case_output_path, 'quality.txt')]
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
def backup(output_path, task_id):
    # task = Task.objects.get(id=task_id)
    results = Results.objects.get(task_id=task_id)
    print("I am backuping {}".format(output_path))
    task.status = 'done'
    task.save()
