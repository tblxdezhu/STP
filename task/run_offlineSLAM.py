#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 2:15 PM
# @Author  : Zhenxuan Xu
# @File    : run_offlineSLAM.py
# @Software: Pycharm professional
import os
import subprocess
import logging
from .SLAM_config import *
import multiprocessing as mp
import shutil


def run_slam(rtv, task_id, mode):
    imu = rtv.replace('.rtv', '.imu')
    case_output_path = os.path.join(output_path, str(task_id), mode, os.path.basename(rtv).strip('.rtv'))
    os.makedirs(case_output_path)
    logging.info("mkdir {}".format(case_output_path))
    vehicle_exec = os.path.join(code_path, "algorithm_vehicle_offlineslam/dist/x64/bin/ZSLAMExe")
    run_cmd_list = [vehicle_exec, '--rtv', rtv, '--iimu', imu, '--ip', slam_config, '--ic', camera_config, '--out', case_output_path]
    # os.chdir(case_output_path)
    run_cmd = ' '.join(run_cmd_list)
    logging.info(run_cmd)
    Run.execute_cmd(run_cmd)


class Run(object):

    def __init__(self, area, task_id):
        self.area = area
        self.task_id = task_id
        self.output_path = os.path.join(output_path, str(self.task_id))

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
        print(find_cmd)
        status, files = subprocess.getstatusoutput(find_cmd)
        files = files.split("\n")
        return files, find_cmd

    @staticmethod
    def execute_cmd(cmd, debug_mode="OFF"):
        if debug_mode == "OFF":
            print(cmd)
            try:
                status, files = subprocess.getstatusoutput(cmd)
            except UnicodeDecodeError:
                pass
        else:
            logging.info(cmd)


class Vehicle(Run):
    def __init__(self, area, task_id):
        super(Vehicle, self).__init__(area, task_id)
        super(Vehicle, self)._check_data()

    def vehicle_slam(self, mode='slam'):
        mp.current_process().daemon = False
        pool = mp.Pool(processes=process_num)
        mp.current_process().daemon = True
        for rtv in self.rtvs:
            imu = rtv.replace('.rtv', '.imu')
            if imu in self.imus:
                pool.apply_async(run_slam, (rtv, self.task_id, mode))

        pool.close()
        pool.join()


class Server(object):
    def __init__(self, vehicle):
        self.server_path = os.path.join(code_path, "algorithm_sam/build/example")
        self._get_server_path()
        self.vehicle = vehicle
        self._serverExampleSLAM_type = '1'

    def _get_server_path(self):
        self.serverExampleSLAM_path = os.path.join(self.server_path, "serverExampleSlam")
        self.section_out = os.path.join(self.server_path, "section_out")
        self.section_db = os.path.join(self.server_path, "section_db")
        self.section = os.path.join(self.server_path, "section")
        self.slamout = os.path.join(self.server_path, "slamout")
        self.gpgga_gps_path = os.path.join(self.server_path, "gpgga_gps")
        self.query_out = os.path.join(self.server_path, "query_out")
        self.query_path = os.path.join(code_path, "algorithm_tools/server/serverExampleQueryDivision/build/querySectionByGps")
        self.extractor = os.path.join(code_path, "../framework/device/rdb-tools-debug-tools/dist/x64/bin/rtv-extractor")
        self.debug_server_path = os.path.join(self.server_path, "server_*")

    @property
    def serverExampleSLAM_type(self):
        return self._serverExampleSLAM_type

    @serverExampleSLAM_type.setter
    def serverExampleSLAM_type(self, value):
        self._serverExampleSLAM_type = value

    def clean(self):
        logging.info("start clean server")

        def __rm(path):
            if os.path.exists(path):
                shutil.rmtree(path)
                logging.info("del {}".format(path))

        __rm(self.section_out)
        __rm(self.section_db)
        __rm(self.slamout)
        __rm(self.section)

    def backup(self, target_path):
        target_path = target_path + "/"
        logging.info("start backup server to {}".format(target_path))
        print(self.section_out,target_path)
        shutil.move(self.section_out, target_path)

        shutil.move(self.section_db, target_path)
        shutil.move(self.section, target_path)
        os.system("mv {} {}".format(self.debug_server_path, target_path))

    def process(self, mode='slam'):
        os.chdir(self.server_path)
        logging.info("start server {}".format(mode))
        if "alignment" in mode:
            self.serverExampleSLAM_type = '2'
        self.serverExampleSLAM(mode)
        os.system("./serverExampleSlam 2 . .")
        self.query()

    def serverExampleSLAM(self, mode):
        logging.info("server running {}".format(mode))
        self._copy_snippets(os.path.join(self.vehicle.output_path, mode), self.server_path, mode)
        cmd_list = [self.serverExampleSLAM_path, self.serverExampleSLAM_type, self.server_path, self.server_path]
        if mode == "slam":
            cmd_list.append(gps_skeleton_path[self.vehicle.area])
        cmd = ' '.join(cmd_list)
        Run.execute_cmd(cmd)

    def query(self):
        logging.info("query")
        cmd_list = [self.query_path, self.gpgga_gps_path, self.section_out, '0']
        cmd = ' '.join(cmd_list)
        Run.execute_cmd(cmd)
        if os.path.exists(self.query_out):
            shutil.rmtree(self.query_out)
            os.mkdir(self.query_out)
        else:
            logging.info("mkdir {}".format(self.query_out))
            os.mkdir(self.query_out)

        for file in os.listdir(self.section):
            with open(os.path.join(self.section, file), 'r') as f:
                rtv_in_query_out = os.path.join(self.query_out, file.strip(".gps"))
                os.mkdir(rtv_in_query_out)
                logging.info("mkdir ".format(rtv_in_query_out))
                dbs = f.readlines()
                for db in dbs:
                    db = db.strip("\n") + ".bin"
                    cmd = "cp " + os.path.join(self.section_out, db) + " " + rtv_in_query_out
                    Run.execute_cmd(cmd)

    @staticmethod
    def _copy_snippets(files_path, output_path, mode):
        logging.info("copy snippet {}".format(mode))
        mode_snippet_type = {"slam": "SlamSnippet*", "alignment": "SlamSnippet*"}
        mode_file_type = {"slam": "maplist.txt", "alignment": "inclist.txt"}
        try:
            output_path = os.path.join(output_path, mode + "out")
            if os.path.exists(output_path):
                shutil.rmtree(output_path)
            os.mkdir(output_path)
            logging.info("mkdir {}".format(output_path))
            for snippet in Run.find_file(files_path, mode_snippet_type[mode])[0]:
                create_path = os.path.join(output_path, snippet.split("/")[-2])
                if not os.path.exists(create_path):
                    os.mkdir(create_path)
                    print("mkdir {}".format(create_path))
                shutil.copy(snippet, os.path.join(create_path, os.path.basename(snippet)))
            os.chdir(os.path.dirname(output_path))
            cmd = "find ./ -name '" + mode_snippet_type[mode] + "' >" + os.path.dirname(output_path) + "/" + \
                  mode_file_type[mode]
            Run.execute_cmd(cmd)
        except IndexError as e:
            print(e)
            print("{} don't have snippets".format(files_path))

    def rtv2gps(self):
        rtv2gpgga_gps_cmd_list = ["find", cases_path[self.vehicle.area], "-name *.rtv -exec", self.extractor, "-f {} -d", self.gpgga_gps_path, "-g \\;"]
        if not os.path.exists(self.gpgga_gps_path):
            logging.info("mkdir {}".format(self.gpgga_gps_path))
            os.mkdir(self.gpgga_gps_path)
        rtv2gpgga_gps_cmd = ' '.join(rtv2gpgga_gps_cmd_list)
        Run.execute_cmd(rtv2gpgga_gps_cmd)
