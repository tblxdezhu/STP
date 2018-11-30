#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/5/18 4:10 PM
# @Author  : Hong He
# @File    : slam_quality.py


'''
define some common function
'''
# from task import SLAM_config
import os
import linecache
import re
import subprocess
from task.SLAM_config import *


class SlamQuality(object):
    static_list_key = ["Type", "RTV", "SLAM_trajectory_length", "GPS_trajectory_length", "Total_number_of_KFs", "Total_frames",
                       "Total_number_of_MPs", "Average_track_length_of_MP", "Weak_convisibility_frame_rate", "MP_per_KF",
                       "Time", "Efficiency", "Total_connections", "Average_error", "Max_error", "Min_error", "Total_count_error",
                       "0~1_count", "1~2_count", "2~5_count", "5~10_count", ">10_count", "<0_count", "Average_offset", "Max_offset",
                       "Min_offset", "Variance_offset", "Total_count_offset", "0~1m_count", "1~2m_count", "2~5m_count", "5~10m_count",
                       "10~20m_count", ">20m_count", "0~100m", "100~300m", "300~500m", "500~1000m", ">1000m"]

    def __init__(self, task_id, area):

        self.quality_path = os.path.join(output_path, str(task_id))
        self.area = str(area)

    def quality_to_dict(self):
        def __find_file(input_path, file_type):
            find_cmd = "find " + input_path + " -name '" + file_type + "'"
            status, files = subprocess.getstatusoutput(find_cmd)
            files = files.split("\n")
            return files

        all_quality_list = list()
        if os.path.exists(self.quality_path):

            areas_quality = dict()
            area_quality_info = list()
            area_quality_path = os.path.join(self.quality_path, str(self.area))
            quality_files = __find_file(area_quality_path, "quality.txt")
            # quality_files = os.listdir(area_quality_path)
            for file_item in quality_files:
                quality_dict = dict()
                quality_lines = linecache.getlines(file_item)

                for line in quality_lines:
                    if line.split(",")[0] in self.static_list_key:
                        quality_dict[line.split(",")[0]] = line.split(",")[1]

                area_quality_info.append(quality_dict)

            areas_quality[str(self.area)] = area_quality_info
            all_quality_list.append(areas_quality)
        else:
            print("Quality path not exist!")

        return all_quality_list


if __name__ == "__main__":
    task_info = {"task_id": 123, "areas": "fuji"}
    slam_obj = SlamQuality(task_info)
    print(slam_obj.quality_to_dict())
