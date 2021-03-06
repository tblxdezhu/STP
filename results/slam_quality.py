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
# from task.SLAM_config import *
from task.models import Task


class SlamQuality(object):
    static_list_key = ["Type", "RTV", "SLAM_trajectory_length", "GPS_trajectory_length", "Total_number_of_KFs", "Total_frames",
                       "Total_number_of_MPs", "Average_track_length_of_MP", "Weak_convisibility_frame_rate", "MP_per_KF",
                       "Time", "Efficiency", "Total_connections", "Projection_error_average", "Projection_error_max", "Projection_error_min", "Projection_error_total_count",
                       "Projection_0~1_count", "Projection_1~2_count", "Projection_2~5_count", "Projection_5~10_count", "Projection_>10_count", "Projection_<0_count", "Offset_average", "Offset_max",
                       "Offset_min", "Offset_variance", "Offset_total_count", "Offset_0~1m_count", "Offset_1~2m_count", "Offset_2~5m_count", "Offset_5~10m_count",
                       "Offset_10~20m_count", "Offset_>20m_count", "MP_distance_0~100m", "MP_distance_100~300m", "MP_distance_300~500m", "MP_distance_500~1000m", "MP_distance_>1000m",
                       "Average_keyframe_number_each_mappoint_see", "Average_mappoint_number_each_keyframe_see", "Average_2D_point_each_keyframe_see", ]

    def __init__(self, task_id, area):

        self.quality_path = Task.objects.get(id=task_id).output_path
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
    slam_obj = SlamQuality(task_id='35', area='15test')
    print(slam_obj.quality_to_dict())
