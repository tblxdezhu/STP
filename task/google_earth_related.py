#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 2:10 PM
# @Author  : Zhenxuan Xu
# @File    : google_earth_related.py
# @Software: Pycharm professional
import os
import re
import paramiko
import stat
from .models import Task
from webserver.models import Machine
import time


class Trajectory:
    def __init__(self, case, kml_name, fill_data, data_type, is_show=True):
        self.is_show = is_show
        self.name = 'a' + ''.join(re.findall('[a-zA-Z0-9]+', kml_name + case))
        self.var_name = "co_" + self.name
        self.prefix = "var coordinates = [".replace("coordinates", self.var_name)
        self.suffix = "];"
        self.data = fill_data
        self.data_processed = []
        self.data_type = data_type
        self.string = '''
                    var name = new google.maps.Polyline({
                      path: coordinates,
                      geodesic: true,
                      strokeColor: '#FF0000',
                      strokeOpacity: 1.0,
                      strokeWeight: 2
                    });           
                    name.setMap(map);
                    '''.replace("name", self.name).replace("coordinates", self.var_name)
        self.write_info = ""

    def string_builder(self):
        for point in self.data:
            list_str = ['{lat:', str(point[1]), ',', 'lng:', str(point[0]), '},']
            self.data_processed.append(' '.join(list_str))
        if self.data_type == 'gps':
            self.string = self.string.replace("'#FF0000'", "'#00FF00'")
        self.write_info = ' '.join([self.prefix, ' '.join(self.data_processed), self.suffix, self.string])
        if self.is_show:
            return self.write_info
        else:
            return ""


def get_scp(task_id):
    machine = Machine.objects.get(machine_id=Task.objects.get(id=task_id).machine_id)
    scp = paramiko.Transport((machine.ip, machine.port))
    scp.connect(username=machine.username, password=machine.password)
    sftp = paramiko.SFTPClient.from_transport(scp)
    return scp, sftp


def data_process(folder_path, task_id):
    start = time.time()
    data = {}
    center = {}
    print("folder_path", folder_path)
    scp, sftp = get_scp(task_id)
    try:
        kmls = get_all_kmls(folder_path, task_id)
    except FileNotFoundError:
        kmls = {}
        scp.close()
        return data, center, kmls
    for k, v in kmls.items():
        data[k] = {}
        for kml in v:
            kml_type = 'slam'
            is_show = True
            kml_name = os.path.basename(kml)
            coordinate = kml2coordinates(kml, sftp)
            if 'gps' in kml_name:
                kml_type = 'gps'
                is_show = False
            trajectory = Trajectory(k, kml_name, coordinate, kml_type, is_show)
            data[k][trajectory.name] = trajectory.string_builder()
            center[k] = trajectory.data_processed[0]
    scp.close()
    end = time.time()
    print("data process cost :", end - start)
    return data, center, kmls


def get_all_kmls(path, task_id):
    data_set = {}
    tmp = ''
    scp, sftp = get_scp(task_id)

    def __get_all_files_in_remote_dir(sftp, remote_dir):
        all_files = []
        remote_files = sftp.listdir_attr(remote_dir)
        for file in remote_files:
            filename = os.path.join(remote_dir, file.filename)
            if stat.S_ISDIR(file.st_mode):
                all_files.extend(__get_all_files_in_remote_dir(sftp, filename))
            else:
                all_files.append(filename)
        return all_files

    for file in __get_all_files_in_remote_dir(sftp, path):
        if file.endswith("final_pose.kml"):
        # if file.endswith("slam_initial_pose.kml"):
            case_name = os.path.basename(os.path.dirname(file))
            if not case_name == tmp:
                data_set[case_name] = []
            data_set[case_name].append(file)
            tmp = case_name
    # try:
    #     for root, dirs, files in os.walk(path):
    #         print("files:",files)
    #         for file in files:
    #             print("file in folder:",file)
    #             # if file.endswith("final_pose.kml") or file.endswith("pre_process_gps.kml"):
    #             if file.endswith("slam_final_pose.kml"):
    #                 # if os.path.basename(root) == "segment":
    #                 # case_name = os.path.dirname(root).split('/')[-3] + "_" + os.path.basename(os.path.dirname(root))
    #                 print("***")
    #                 print("root", root)
    #                 print("file", file)
    #                 print("***")
    #                 case_name = root.split('/')[-2] + "_" + os.path.basename(root)
    #                 print("case_name", case_name)
    #                 if not case_name == tmp:
    #                     data_set[case_name] = []
    #                 data_set[case_name].append(os.path.join(root, file))
    #                 tmp = case_name
    # except Exception as e:
    #     print(e)
    scp.close()
    print("data_set", data_set)
    return data_set


def kml2coordinates(file_path, sftp):
    # scp, sftp = get_scp(task_id)
    # scp = paramiko.Transport(('10.69.142.68', 22))
    # scp.connect(username='roaddb', password='test1234')
    # sftp = paramiko.SFTPClient.from_transport(scp)
    f = sftp.open(file_path, 'r+')
    lines = f.readlines()
    f.close()
    # with open(file_path) as f:
    #     lines = f.readlines()
    coordinates = []
    for line in lines:
        if line.strip().startswith('<'):
            continue
        try:
            for coordinate in line.strip().split():
                lon, lat, alt = coordinate.split(',')
                coordinates.append((float(lon), float(lat)))
        except Exception as e:
            print("converting gps wrongly !!!")
            print(e)
            continue
    return coordinates
