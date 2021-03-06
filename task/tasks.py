#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/30 3:11 PM
# @Author  : Zhenxuan Xu
# @File    : tasks.py
# @Software: Pycharm professional

from celery import task
import time
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


# from STP2.settings import get_branchs_code_path


def build(branchs, task_id, if_build=True, mode='slam', build_sam=False):
    if not mode == "slam":
        build_sam = True
    if if_build:
        print(branchs)
        task = Task.objects.get(id=task_id)
        task.status = 'build'
        task.save()
        branchs['is_sam'] = build_sam
        compile_code = Compile_code(branchs, task_id)
        print("code path2:", compile_code.compile_info["code_path"])
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
    task = Task.objects.get(id=task_id)
    machine = Machine.objects.get(machine_id=get_machine_id())
    task.code_path = machine.code_path
    task.machine_id = get_machine_id()
    task.output_path = os.path.join(machine.output_path, str(task.id))
    task.save(update_fields=['code_path', 'machine_id', 'output_path'])

    def __change_status(task_id, status):
        task = Task.objects.get(id=task_id)
        task.status = status
        # save() 方法会设定所有列的 值，而不是只设定 name 列的值。
        # 如果你所处的环境可能同时由其他操作修改其他列，最好只更新需要修改的值。
        # 为此，使用 QuerySet 对象的 update() 方法
        # TODO 需要将不必要的save替换为update
        task.save(update_fields=['status'])
        logging.info("status change to {}".format(status))

    # COMPILE THE CODE , DEFAULT MODE IS NOT BUILD ALGO_SAM
    build(eval(task.branch), task_id, if_build)
    rtv_num = 0
    for area in eval(task.area):
        run = Run(area, task_id)
        rtv_num = rtv_num + run.rtv_num
    task.total_rtv = rtv_num
    task.save(update_fields=['total_rtv', ])

    for area in eval(task.area):
        vehicle = Vehicle(str(area), task.id)
        __change_status(task_id, 'SLAM')
        try:
            vehicle.vehicle_slam()
            __change_status(task_id, 'SLAMdone')

            task_result = SlamQuality(task_id, area).quality_to_dict()

            for case_result in task_result[0][area]:
                print("case_result:", case_result)
                if case_result:
                    result = Results.objects.create(
                        task_id=task.id, area=area, mode='slam', rtv_name=case_result['RTV'], slam_len=case_result['SLAM_trajectory_length'], gps_len=case_result['GPS_trajectory_length'],
                        kfs=case_result['Total_number_of_KFs'], rtv_frames=case_result['Total_frames'], mps=case_result['Total_number_of_MPs'],
                        avg_track_len_mp=case_result['Average_track_length_of_MP'], weak_rate=case_result['Weak_convisibility_frame_rate'],
                        mp_kf=case_result['MP_per_KF'], time=case_result['Time'], efficiency=case_result['Efficiency']
                    )

        except Exception as e:
            print(e)
            __change_status(task_id, 'SLAMfailed')

    if task.mode == 'SSA':
        build(eval(task.branch), task_id, if_build, task.mode)

        for area in eval(task.area):
            server = Server(str(area), task.id)
            __change_status(task_id, 'SSA')
            try:
                server.clean()
                server.rtv2gps()
                server.process()
                __change_status(task_id, 'SSAdone')
                __change_status(task_id, 'backup')
                try:
                    server.backup()
                    __change_status(task_id, 'backupdone')
                except Exception as e:
                    print(e)
                    __change_status(task_id, 'backupfailed')
            except Exception as e:
                print(e)
                __change_status(task_id, 'SSAfailed')
        # __change_status('done')

# @task
# def get_branch():
#     repo_list = ['common', 'algorithm_common', 'algorithm_vehicle_offlineslam', 'algorithm_sam']
#     for repo in repo_list:
#         os.chdir(os.path.join(get_branchs_code_path, repo))
#         print(repo)
#         status, output = subprocess.getstatusoutput("git branch -a")
#         print(output)
