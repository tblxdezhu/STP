# -*- coding: utf-8 -*-
# !/usr/bin/env python
# encoding: utf-8
# @Time    : 10/22/18 5:39 PM
# @Author  : Hong He
# @File    : compile_code.py


'''
define some common function
'''
import paramiko
import os
import subprocess
# from .build_config import code_path
from .models import Task


class Compile_code(object):
    compile_info = {}

    def __init__(self, branchs, task_id):
        self.task = Task.objects.get(id=task_id)
        if branchs["is_sam"]:
            self.compile_info["is_sam"] = True
            self.compile_info["algorithm_sam"] = branchs["algorithm_sam"]
        else:
            self.compile_info["is_sam"] = False
            self.compile_info["algorithm_vehicle_offlineslam"] = branchs["algorithm_vehicle_offlineslam"]

        if branchs.__contains__("commit_point") and branchs["commit_point"]:
            self.compile_info["commit_point"] = branchs["commit_point"]
        else:
            self.compile_info["commit_point"] = ""

        self.compile_info["code_path"] = self.task.code_path
        self.compile_info["common"] = branchs["common"]
        self.compile_info["algorithm_common"] = branchs["algorithm_common"]
        self.compile_info["algorithm_common_slam"] = branchs["algorithm_common_slam"]
        self.compile_info["vehicle"] = branchs["vehicle"]

        self.compile_info["stash_common"] = "ssh://git@stash.ygomi.com:7999/rc/common.git"
        self.compile_info["stash_algo_common"] = "ssh://git@stash.ygomi.com:7999/rc/algorithm_common.git"
        self.compile_info["stash_algo_common_slam"] = "ssh://git@stash.ygomi.com:7999/rc/algorithm_common_slam.git"
        self.compile_info["stash_algo_vehicle_offlineslam"] = "ssh://git@stash.ygomi.com:7999/rc/algorithm_vehicle_offlineslam.git"
        self.compile_info["stash_algo_sam"] = "ssh://git@stash.ygomi.com:7999/rc/algorithm_sam.git"
        self.compile_info["stash_vehicle"] = "ssh://git@stash.ygomi.com:7999/rc/vehicle.git"

    def __compile_cmds__(self, code_path, repo_name, stash_addr, branch_name, commit_point, parameters=""):

        cmds_dict = dict()
        cmds_dict["clear_repo_cmd"] = "rm -rf {0}".format(os.path.join(code_path, repo_name))
        cmds_dict["git_clone"] = "cd {0} && git clone {1}".format(code_path, stash_addr)
        cmds_dict["git_checkout_cmd"] = "cd {0} && git checkout {1} && git pull".format(os.path.join(code_path, repo_name), branch_name)
        cmds_dict["git_commit_point"] = " git reset --hard {0}".format(commit_point)

        # if algo-common repo should close deep-learning.
        if repo_name == "algorithm_common":

            cmds_dict["update_cmakelist"] = "sed -i 's/\"compile deeplearning interface\" ON/\"compile deeplearning interface\" OFF/g' {}".format(
                os.path.join(self.compile_info["code_path"], "algorithm_common", "CMakeLists.txt"))
        else:
            cmds_dict["update_cmakelist"] = ""

        # Vehicle repo do not compile , delete files and clone code
        if "vehicle" == repo_name:
            cmds_dict["compile_cmd"] = ""
            cmds_dict["clear_repo_cmd"] = ""
            cmds_dict["git_clone"] = ""
        else:
            cmds_dict["compile_cmd"] = "./build.sh {0}".format(parameters)
        return cmds_dict

    def __ssh_run_cmd__(self, cmds):

        results = dict()
        try:
            cmd = cmds["clear_repo_cmd"] + ";" + cmds["git_clone"] + ";" + cmds["git_checkout_cmd"]

            if cmds["git_commit_point"]:
                cmd += ";" + cmds["git_commit_point"]
            else:
                pass

            if cmds["update_cmakelist"]:
                cmd += ";" + cmds["update_cmakelist"]
            else:
                pass

            cmd += ";" + cmds["compile_cmd"]

            print(cmd)
            subprocess.getstatusoutput(cmd)

            return results
        except:
            print("Connect virtual machine failed!")
            raise

    def __compile_common(self):

        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "common",
                                     self.compile_info["stash_common"],
                                     self.compile_info["common"], "")

        compile_result = self.__ssh_run_cmd__(cmds)

        return compile_result

    def __compile_algo_common(self):

        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "algorithm_common",
                                     self.compile_info["stash_algo_common"],
                                     self.compile_info["algorithm_common"], "",
                                     "-s")

        compile_result = self.__ssh_run_cmd__(cmds)

        return compile_result

    def __compile_algo_common_slam(self):

        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "algorithm_common_slam",
                                     self.compile_info["stash_algo_common_slam"],
                                     self.compile_info["algorithm_common_slam"], "")

        compile_result = self.__ssh_run_cmd__(cmds)

        return compile_result

    def __compile_algo_offlineslam(self):

        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "algorithm_vehicle_offlineslam",
                                     self.compile_info["stash_algo_vehicle_offlineslam"],
                                     self.compile_info["algorithm_vehicle_offlineslam"],
                                     self.compile_info["commit_point"],
                                     "-ed")
        # print(cmds)
        compile_result = self.__ssh_run_cmd__(cmds)
        return compile_result

    def __compile_algo_sam(self):
        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "algorithm_sam",
                                     self.compile_info["stash_algo_sam"],
                                     self.compile_info["algorithm_sam"],
                                     self.compile_info["commit_point"],
                                     "-g")
        compile_result = self.__ssh_run_cmd__(cmds)
        return compile_result

    def __compile_vehicle(self):
        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "vehicle",
                                     self.compile_info["stash_vehicle"],
                                     self.compile_info["vehicle"],
                                     self.compile_info["commit_point"],
                                     "-g")
        compile_result = self.__ssh_run_cmd__(cmds)
        return compile_result

    def run_compile(self):
        try:
            result_common = self.__compile_common()
        except UnicodeDecodeError:
            pass

        result_algo_common = self.__compile_algo_common()
        result_algo_common_slam = self.__compile_algo_common_slam()

        result_algo = ""
        # print(self.compile_info["is_sam"])
        if not self.compile_info["is_sam"]:
            result_algo = self.__compile_algo_offlineslam()
        else:
            result_algo = self.__compile_algo_sam()
        result_vehicle = self.__compile_vehicle()


if __name__ == "__main__":
    branchs = {"common": "feature/RDB-33158-release-of-offline-slam",
               "algorithm_common": "feature/RDB-33158-release-of-offline-slam",
               "algorithm_vehicle_offlineslam": "feature/RDB-33158-release-of-offline-slam",
               "is_sam": False}
    obj_compile = Compile_code(branchs)
    obj_compile.run_compile()
