#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/06/2018 1:57 PM
# @Author  : Zhenxuan Xu
# @Site    : 
# @File    : run_offlineSLAM.py
# @Software: PyCharm

import os
import sys
import shutil
import logging
import subprocess
import datetime
from functools import wraps
from .common_interface import Interface_run
from .common_interface import Config
from .common_interface import MyException
from .common_interface import Logger
from multiprocessing import Pool

# from tools.utils import cheese
import coloredlogs

# FORMAT = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
# logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = Logger(log_name="test.log", logger="test").get_log()
coloredlogs.install(level='DEBUG', logger=logger)


def logged(msg=None):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = msg if msg else func(*args, **kwargs)
            logger.info(results[1])
            return results

        return wrapper

    return decorate


class Common(object):

    @staticmethod
    @logged()
    def find_file(input_path, file_type):

        find_cmd = "find " + input_path + " -name '" + file_type + "'"
        status, files = subprocess.getstatusoutput(find_cmd)
        if not status == 0:
            raise MyException
        files = files.split("\n")
        return files, find_cmd

    @staticmethod
    @logged()
    def execute_cmd(cmd, mode="OFF"):
        if mode == "OFF":
            status, output = subprocess.getstatusoutput(cmd)
            if status == 0:
                pass
            else:
                logger.error(output)
            return status, "run over {}".format(cmd)
        else:
            logger.info(cmd)


class Run(Interface_run):
    # __slots__ = ['cases_path', 'rtvs', 'imus', 'source_path', 'vehicle_exec', 'server_path', 'config_file',
    #              'output_path', 'process_num', 'if_semi', 'branch', 'area', 'script_mode', 'date', 'output', 'if_db',
    #              'log_name', 'serverExampleSLAM_path', 'section_out', 'section_db', 'section', 'gps_skeleton_path']
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    def __init__(self, parsers=Config.content()):
        self.slam_version = parsers.get("slam_version")
        self.cases_path = parsers.get("cases")
        self.source_path = parsers.get("source_code_path")
        self.vehicle_exec = os.path.join(self.source_path, "core/algorithm_vehicle/vehicle/offlineSLAM/bin/ZSLAMExe")
        self.server_path = os.path.join(self.source_path, "core/algorithm_sam/build/example")
        self.gps_skeleton_path = parsers.get("gps_skeleton_path")
        self.output_path = parsers.get("output_path")
        self.process_num = parsers.get("process_num")
        self.if_semi = parsers.get("generate_semi")
        self.branch = parsers.get("branch")
        self.area = parsers.get("area")
        self.script_mode = parsers.get("mode")
        # self.date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        self._output = os.path.join(self.output_path, '_'.join([Run.date, self.slam_version, str(self.branch), self.area]))
        self.if_db = parsers.get("backup_data_to_database")
        self._log_name = '_'.join([Run.date, self.area, self.branch, '.log'])
        self.config_file = os.path.join(self.source_path, "core/algorithm_vehicle/vehicle/offlineSLAM/config", parsers.get("config_file"))

    @property
    def log_name(self):
        return self._log_name

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

    @classmethod
    def _if_backup_to_db(cls):
        if cls().if_db:
            print
            "backup data to database"
        else:
            print
            "don't backup data to db , exit "
            sys.exit(0)

    def _get_cases(self):
        self.rtvs, self.imus = self.__get_data(self.cases_path)

    def _get_server_path(self):
        self.serverExampleSLAM_path = os.path.join(self.server_path, "serverExampleSlam")
        self.section_out = os.path.join(self.server_path, "section_out")
        self.section_db = os.path.join(self.server_path, "section_db")
        self.section = os.path.join(self.server_path, "section")
        self.gpgga_gps_path = os.path.join(self.server_path, "gpgga_gps")
        self.query_out = os.path.join(self.server_path, "query_out")
        self.query_path = os.path.join(self.source_path, "core/algorithm_tools/server/serverExampleQueryDivision/build/querySectionByGps")
        self.extractor = os.path.join(self.source_path, "framework/device/rdb-tools-debug-tools/dist/x64/bin/rtv-extractor")

    def _script_mode(self):
        return self.script_mode

    def _get_date(self):
        return Run.date

    def _get_branch(self):
        return self.branch

    def _get_output(self):
        return self.output

    def __get_data(self, data_path):
        rtvs_list = Common.find_file(data_path, "*.rtv")
        imus_list = Common.find_file(data_path, "*.imu")
        return rtvs_list[0], imus_list[0]

    def _check_data(self):
        self._get_cases()
        diff_list = list(set(self.rtvs) ^ set([imu.replace(".imu", ".rtv") for imu in self.imus]))
        try:
            if diff_list:
                raise ValueError
            else:
                logger.info("rtv and imu matched")
        except ValueError:
            logger.error("rtvs and imus are not match {}".format(diff_list))


def run_slam(rtv, imu, gps, output_path, config, mode, vehicle_exec, server_path, if_semi=False):
    # cheese()
    os.makedirs(output_path)
    logger.info("mkdir {}".format(output_path))
    run_cmd_list = [vehicle_exec, '--rtv', rtv, '--iimu', imu, '--ip', config]
    if if_semi:
        run_cmd_list.extend(['--d', output_path])
    if not mode == "slam":
        db_path = os.path.join(server_path, "query_out", os.path.basename(rtv))
        run_cmd_list.extend(['--idb', db_path])
    run_cmd = ' '.join(run_cmd_list)
    os.chdir(output_path)
    logger.info(run_cmd)
    Common.execute_cmd(run_cmd)


class Vehicle(Run):
    def __init__(self):
        super(Vehicle, self).__init__()
        super(Vehicle, self)._get_cases()

    def vehicle_slam(self, vehicle_mode='slam'):
        logger.info("start to run {}".format(vehicle_mode))
        pool = Pool(processes=self.process_num)
        for rtv in self.rtvs:
            imu = rtv.replace('.rtv', '.imu')
            gps = rtv.replace('.rtv', '.txt')
            if not os.path.exists(gps):
                logger.info("mknod gps")
                os.mknod(gps)
            output_path = os.path.join(Run().output, vehicle_mode, os.path.basename(rtv).strip('.rtv'))
            if imu in self.imus:
                pool.apply_async(run_slam, (
                    rtv, imu, gps, output_path, self.config_file, vehicle_mode, self.vehicle_exec, self.server_path,
                    self.if_semi,))
        pool.close()
        pool.join()

    @classmethod
    def slam(cls):
        cls().vehicle_slam()

    @classmethod
    def alignment(cls):
        cls().vehicle_slam(vehicle_mode="alignment")

    @classmethod
    def alignment2(cls):
        cls().vehicle_slam(vehicle_mode="alignment2")

    @classmethod
    def rt(cls):
        cls().vehicle_slam(vehicle_mode="rt")


class Server(Run):
    def __init__(self):
        # TODO 检查这里的逻辑，会导致重复实例化
        super(Server, self).__init__()
        super(Server, self)._get_server_path()
        self._serverExampleSLAM_type = '1'

    @property
    def serverExampleSLAM_type(self):
        return self._serverExampleSLAM_type

    @serverExampleSLAM_type.setter
    def serverExampleSLAM_type(self, value):
        self._serverExampleSLAM_type = value

    @classmethod
    def clean(cls):
        logger.info("start clean server")

        def __rm(path):
            if os.path.exists(path):
                shutil.rmtree(path)
                logger.info("rm {}".format(path))

        __rm(cls().section_out)
        __rm(cls().section_db)
        __rm(cls().section)

    @classmethod
    def process(cls, mode='slam', resetConfidence=False):
        os.chdir(cls().server_path)
        logger.info("start server {}".format(mode))
        if "alignment" in mode:
            cls.serverExampleSLAM_type = '2'
        cls.serverExampleSLAM(mode)
        os.system("./serverExampleSlam 2 . .")
        if resetConfidence:
            cls.resetConfidence()
        # cls.query()

    @classmethod
    def serverExampleSLAM(cls, mode):
        logger.info("server running {}".format(mode))
        cls._copy_snippets(os.path.join(cls.output, mode), cls().server_path, mode)
        cmd_list = [cls().serverExampleSLAM_path, cls().serverExampleSLAM_type, cls().server_path, cls().server_path]
        if mode == "slam":
            cmd_list.append(cls().gps_skeleton_path)
        cmd = ' '.join(cmd_list)
        Common.execute_cmd(cmd)

    @classmethod
    def query(cls):
        logger.info("query")
        cmd_list = [cls().query_path, cls().gpgga_gps_path, cls().section_out]
        cmd = ' '.join(cmd_list)
        Common.execute_cmd(cmd)
        if os.path.exists(cls().query_out):
            shutil.rmtree(cls().query_out)
            os.mkdir(cls().query_out)
        else:
            logger.info("mkdir {}".format(cls().query_out))
            os.mkdir(cls().query_out)

        for file in os.listdir(cls().section):
            with open(os.path.join(cls().section, file), 'r') as f:
                rtv_in_query_out = os.path.join(cls().query_out, file.strip(".gps"))
                os.mkdir(rtv_in_query_out)
                logger.info("mkdir ".format(rtv_in_query_out))
                dbs = f.readlines()
                for db in dbs:
                    db = db.strip("\n") + ".bin"
                    cmd = "cp " + os.path.join(cls().section_out, db) + " " + rtv_in_query_out
                    Common.execute_cmd(cmd)

    @classmethod
    def resetConfidence(cls):
        logger.info("resetConfidence")
        cmd_list = [cls().serverExampleSLAM_path, '3', cls().server_path, cls().server_path, '105']
        cmd = ' '.join(cmd_list)
        Common.execute_cmd(cmd)

    @staticmethod
    def _copy_snippets(files_path, output_path, mode):
        # TODO Need to optimize
        logger.info("copy snippet {}".format(mode))
        mode_snippet_type = {"slam": "SlamSnippet*", "alignment": "SlamSnippet*", "rt": "SlamSnippet*", "alignment2": "SlamSnippet*"}
        mode_file_type = {"slam": "maplist.txt", "alignment": "inclist.txt", "alignment2": "inclist.txt"}

        if mode == "alignment2":
            mode = "alignment"
        print
        output_path
        output_path = os.path.join(output_path, mode + "out")
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        os.mkdir(output_path)
        logger.info("mkdir {}".format(output_path))
        for snippet in Common.find_file(files_path, mode_snippet_type[mode])[0]:
            create_path = os.path.join(output_path, snippet.split("/")[-2])
            if not os.path.exists(create_path):
                os.mkdir(create_path)
                print
                "mkdir {}".format(create_path)
            shutil.copy(snippet, os.path.join(create_path, os.path.basename(snippet)))
        os.chdir(os.path.dirname(output_path))
        cmd = "find ./ -name '" + mode_snippet_type[mode] + "' >" + os.path.dirname(output_path) + "/" + \
              mode_file_type[mode]
        Common.execute_cmd(cmd)


@classmethod
def rtv2gps(cls):
    rtv2gpgga_gps_cmd_list = ["find", cls().cases_path, "-name *.rtv -exec", cls().extractor, "-f {} -d", cls().gpgga_gps_path, "-g \\;"]
    if not os.path.exists(cls().gpgga_gps_path):
        logger.info("mkdir {}".format(cls().gpgga_gps_path))
        os.mkdir(cls().gpgga_gps_path)
    rtv2gpgga_gps_cmd = ' '.join(rtv2gpgga_gps_cmd_list)
    Common.execute_cmd(rtv2gpgga_gps_cmd)


class ProcessControl(Run):
    def __init__(self):
        super(ProcessControl, self).__init__()

    @classmethod
    def decide_mode(cls):
        def str_func(mode):
            return "ProcessControl._{}()".format(mode)

        print
        cls().script_mode
        eval(str_func(cls().script_mode))

    @staticmethod
    def _slam():
        Vehicle.slam()

    @staticmethod
    def _alignment():
        Run.output = Config.slam_output_path()
        Server.clean()
        # Server.rtv2gps()
        Server.process()
        # Vehicle.alignment()
        # Server.process(mode="alignment")
        # Vehicle.alignment2()
        # Server.process(mode="alignment2", resetConfidence=True)
        # Vehicle.rt()

    @staticmethod
    def _alignment2():
        Server.rtv2gps()
        Server.process(mode='slam')
        Vehicle.alignment2()
        Server.process(resetConfidence=True)
        Vehicle.rt()

    @staticmethod
    def _rt():
        Server.rtv2gps()
        Server.process(resetConfidence=True)
        Vehicle.rt()

    @staticmethod
    def _all():
        Vehicle.slam()
        Server.clean()
        # Server.rtv2gps()
        Server.process()
        # Vehicle.alignment()
        # Server.process(mode="alignment")
        # Vehicle.alignment2()
        # Server.process(mode="alignment2", resetConfidence=True)
        # Vehicle.rt()


if __name__ == '__main__':
    run = Run()
    run._start()
