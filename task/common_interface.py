#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 01/06/2018 4:40 PM
# @Author  : Zhenxuan Xu
# @Site    : 
# @File    : common_interface.py
# @Software: PyCharm

from abc import ABCMeta, abstractmethod
import numpy as np
from optparse import OptionParser
import yaml
import logging


class MyException(Exception):
    def __init__(self, err=""):
        Exception.__init__(self, err)


class Interface_run(object):
    def _start(self):
        self._check_data()
        from .run_offlineSLAM import ProcessControl
        ProcessControl.decide_mode()
        self._if_backup_to_db()
        # self._run_slam()
        # self._if_backup_to_db()

    def _get_info(self):
        """
        get info of data such as the name of rtv and commit point
        :return: None
        """
        return self._get_date(), self._get_branch(), self._get_output()


class Interface_data():
    # __metaclass__ = ABCMeta

    def _get_info(self):
        """
        get info of data such as the name of rtv and commit point
        :return: None
        """
        return self._get_date(), self._get_branch(), self._get_output()

    def _get_data(self):
        """
        define interface
        :return:
        """
        self._read_quality()
        self._data_process()

    # the abstractmethod doesn't seem to need it

    # @abstractmethod
    # def save_data(self):
    #     """
    #     save data to database
    #     :return: None
    #     """


class Interface_out():
    def _out(self):
        self._draw()
        self._send_email()


class Logger:
    def __init__(self, log_name, logger, level=logging.DEBUG):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level)
        file_handler = logging.FileHandler(log_name)
        file_handler.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        file_handler.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger


class Config:
    @staticmethod
    def get_parser():
        parser = OptionParser(usage="%prog [-i] [-o]", version="%prog 1.1")
        parser.add_option("-i", dest="config_file", default="config.yaml", help="The config file of test")
        parser.add_option("-o", dest="slam_output_path", default="~/xuzhenxuan/outputs/", help="The path of SLAM output , you must input this parser if you choose the alignment mode")
        (options, args) = parser.parse_args()
        return options.config_file, options.slam_output_path

    @classmethod
    def content(cls):
        with open(cls().get_parser()[0], 'r') as f:
            y = yaml.load(f)
            return y

    @classmethod
    def slam_output_path(cls):
        return cls().get_parser()[1]


def tran_list(quality_data, n):
    """
    Get the n column in the quality.txt file
    :param quality_data:the data read from quality.txt
    :param n:which column you want
    :return:type list
    """
    arr = np.array(quality_data, dtype=np.float64)
    return arr[:, n - 1].flatten().tolist()


##########################################################################################
# EXAMPLE HOW TO USE tran_list
# dic = {
#     "kf_id": tran_list(quality, 1),
#     "Covisibility": tran_list(quality, 2),
#     "pts_num": tran_list(quality, 3),
#     "Avg_reproj_err": tran_list(quality, 4),
#     "Dist_to_GPS": tran_list(quality, 5)
# }
##########################################################################################

def get_parse():
    """
    Parse the input parameters
    :return:the path of input
            the config file
            the path of output
            the number of process
            the mode of run script
    """
    parser = OptionParser(usage="%prog [-i] [-c] [-o] [-n]", version="%prog 1.0")
    parser.add_option("-m", dest="mode", default='SLAM', help="The Mode")
    parser.add_option("-i", dest="input_path", help="The Input Path")
    parser.add_option("-c", dest="config", help="The Config File of Camera")
    parser.add_option("-o", dest="output_path", help="The Output Path", )
    parser.add_option("-n", dest="process_number", help="The Process number")
    (options, args) = parser.parse_args()
    # TODO add except
    return options.input_path, options.config, options.output_path, int(options.process_number), options.mode
