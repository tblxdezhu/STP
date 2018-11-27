#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 2:15 PM
# @Author  : Zhenxuan Xu
# @File    : run_offlineSLAM.py
# @Software: Pycharm professional
import os
import datetime
import subprocess
import logging
from .SLAM_config import *
import multiprocessing as mp
import time
import pickle


def run_slam(rtv):
    imu = rtv.replace('.rtv', '.imu')
    case_output_path = os.path.join(output_path, "slam", os.path.basename(rtv).strip('.rtv'))
    print(os.getpid())
    mp.current_process().daemon = True
    os.makedirs(case_output_path)
    logging.info("mkdir {}".format(case_output_path))
    run_cmd_list = [vehicle_exec, '--rtv', rtv, '--iimu', imu, '--ip', slam_config, '--ic', camera_config]
    os.chdir(case_output_path)
    run_cmd = ' '.join(run_cmd_list)
    logging.info(run_cmd)
    Run.execute_cmd(run_cmd)
    # Run.execute_cmd('/Users/test1/PycharmProjects/github/STP/test.sh')


class Run(object):
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    def __init__(self, area, mode, tester):
        self.area = area
        self.mode = mode
        self.tester = tester
        self.output_path = os.path.join(output_path, self.tester, self.area, Run.date)

    def _check_data(self):
        self.__get_cases()
        diff_list = list(set(self.rtvs) ^ set([imu.replace(".imu", ".rtv") for imu in self.imus]))
        try:
            if diff_list:
                raise ValueError
            else:
                logging.info("rtv and imu matched")
        except ValueError:
            logging.error("rtvs and imus are not match {}".format(diff_list))

    def __get_cases(self):
        self.rtvs, self.imus = self.__get_data(cases_path[self.area])

    @staticmethod
    def __get_data(data_path):
        rtvs_list = Run.find_file(data_path, "*.rtv")
        imus_list = Run.find_file(data_path, "*.imu")
        return rtvs_list[0], imus_list[0]

    @staticmethod
    def find_file(input_path, file_type):
        find_cmd = "find " + input_path + " -name '" + file_type + "'"
        status, files = subprocess.getstatusoutput(find_cmd)
        files = files.split("\n")
        return files, find_cmd

    @staticmethod
    def execute_cmd(cmd, debug_mode="OFF"):
        if debug_mode == "OFF":
            subprocess.call(cmd, shell=True)
        else:
            logging.info(cmd)


class Vehicle(Run):
    def __init__(self, area, tester, mode="SLAM"):
        super(Vehicle, self).__init__(area, mode, tester)
        super(Vehicle, self)._check_data()

    def vehicle_slam(self, mode='slam'):

        mp.current_process().daemon = False
        pool = mp.Pool(processes=process_num)
        print("PID >>>>>>>>>>>", os.getpid())
        # curr_proc.daemon = False
        mp.current_process().daemon = True
        # curr_proc.daemon = True
        print("PPID >>>>>>>>>>>", os.getppid())
        sent_list = []
        for rtv in self.rtvs:

            imu = rtv.replace('.rtv', '.imu')
            case_output_path = os.path.join(self.output_path, mode, os.path.basename(rtv).strip('.rtv'))
            if imu in self.imus:
                # pool.apply_async(run_slam, (rtv, imu, slam_config, camera_config, case_output_path))
                sent_list.append(rtv)
        print(sent_list)
        pool.map(run_slam, sent_list)
        # print("poor will be terminate soon")
        # time.sleep(5)
        # self.terminate_poor()

        pool.close()
        pool.join()
