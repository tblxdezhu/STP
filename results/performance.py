#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:46 AM
# @Author  : Zhenxuan Xu
# @File    : performance.py
# @Software: Pycharm professional

import numpy as np
from math import radians, cos, sin, asin, sqrt


class Kml(object):
    def __init__(self, kml_path):
        self.kml_path = kml_path
        self.points = self.__kml2coordinates()

    def __kml2coordinates(self):
        with open(self.kml_path) as f:
            lines = f.readlines()
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

    @property
    def xy(self):
        return np.array(self.points)[:, 0], np.array(self.points)[:, 1]


class Calculate(object):
    def __init__(self, slam_kml, gps_kml):
        self.slam_kml = slam_kml
        self.gps_kml = gps_kml

    @staticmethod
    def get_points(kml):
        return Kml(kml_path=kml).points

    def get_distance_list(self):
        try:
            print(self.get_points(self.slam_kml))
            print(self.get_points(self.gps_kml))
            if not len(self.get_points(self.slam_kml)) == len(self.get_points(self.gps_kml)):
                raise IndexError
            else:
                return [self._cal_distance(self.get_points(self.slam_kml)[i], self.get_points(self.gps_kml)[i]) for i in range(len(self.get_points(self.slam_kml)))]
        except IndexError:
            print("the points in slam and gps kml were not equal")
            print("slam.kml : {}".format(len(self.get_points(self.slam_kml))))
            print("gps.kml : {}".format(len(self.get_points(self.gps_kml))))
            return [self._cal_distance(self.get_points(self.slam_kml)[i], self.get_points(self.gps_kml)[i+3]) for i in range(len(self.get_points(self.slam_kml)))]

    @staticmethod
    def _cal_distance(point_1, point_2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        lon1, lat1 = point_1
        lon2, lat2 = point_2
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r * 1000

    def cal_rmse(self):
        """
        Root Mean Square Error
        :return:
        """
        data = np.array(self.get_distance_list())
        return np.sqrt(np.sum(data ** 2) / len(data))


if __name__ == '__main__':
    cal = Calculate(slam_kml="slam_final_pose.kml", gps_kml="slam_pre_process_gps.kml")
    print(cal.cal_rmse())
