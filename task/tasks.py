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
import subprocess
import pickle
from .models import Task
import datetime
from .compile_code import Compile_code
from results.models import Results, Overview
from results.slam_quality import SlamQuality
from webserver.models import Machine
from STP2.settings import get_branchs_code_path
import traceback


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


def get_machine_id():
    _, machine_id = subprocess.getstatusoutput("cat /var/lib/dbus/machine-id")
    return machine_id


@task
def work_flow(if_build, task_id):
    print("in work flow >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    task = Task.objects.get(id=task_id)
    machine = Machine.objects.get(machine_id=get_machine_id())
    task.code_path = machine.code_path
    task.machine_id = machine.machine_id
    task.output_path = os.path.join(machine.output_path, str(task.id))
    task.save()
    print("machine_id:", get_machine_id())
    print("type:", type(get_machine_id()))
    print("output path:", task.output_path)

    def __change_status(status):
        task.status = status
        # save() 方法会设定所有列的 值，而不是只设定 name 列的值。
        # 如果你所处的环境可能同时由其他操作修改其他列，最好只更新需要修改的值。
        # 为此，使用 QuerySet 对象的 update() 方法
        # TODO 需要将不必要的save替换为update
        task.save()
        logging.info("status change to {}".format(status))

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
            print(traceback.print_exc())
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
                    __change_status('backupdone')
                except Exception as e:
                    print(e)
                    __change_status('backupfailed')
            except Exception as e:
                print(e)
                __change_status('SSAfailed')
        # __change_status('done')


@task
def get_branch():
    repo_list = ['common', 'algorithm_common', 'algorithm_vehicle_offlineslam', 'algorithm_sam']
    for repo in repo_list:
        os.chdir(os.path.join(get_branchs_code_path, repo))
        print(repo)
        status, output = subprocess.getstatusoutput("git branch -a")
        print(output)