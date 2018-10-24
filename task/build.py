#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 3:16 PM
# @Author  : Zhenxuan Xu
# @File    : build.py
# @Software: Pycharm professional
import os
import paramiko
from .build_config import *


# class Build(object):
#     build_order = ['common', 'algorithm_common', 'algorithm_vehicle_offlineslam']
#
#     def __init__(self, task_id, branchs):
#         self.task_id = task_id
#         self.branchs = branchs
#         self.work_path = os.path.join(code_path, 'core')
#         self.clear()
#
#     def clone(self):
#         os.chdir(self.work_path)
#
#     def pull(self):
#
#         def checkout(branch):
#             return "git checkout {} && git pull".format(branch)
#
#         for repo in Build.build_order:
#             os.chdir(os.path.join(self.work_path, repo))
#
#     def clear(self):
#         self.__ssh_run_cmd(ip, "rm -rf {}/*".format(self.work_path))
#
#     @staticmethod
#     def __ssh_run_cmd(ssh_ip, cmd, username="roaddb", password="test1234"):
#         client = None
#         results = dict()
#         try:
#             client = paramiko.SSHClient()
#             client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             client.connect(ssh_ip, 22, username=username, password=password, compress=True)
#             stdin_compile, stdout_compile, stderr_compile = client.exec_command(command=cmd)
#             results["compile_cmd"] = stdout_compile.channel.recv_exit_status()
#             results["compile_cmd_detail"] = stdout_compile.readlines()
#             return results
#         except Exception as e:
#             print("Connect virtual machine failed!")
#             raise e
#         finally:
#             client.close()


class Compile(object):
    def __init__(self, task_id, branchs):
        self.task_id = task_id
        self.branchs = branchs

    @staticmethod
    def __compile_cmds(code_path, repo_name, stash_addr, branch_name, commit_point="", parameters=""):
        cmds_dict = dict()
        cmds_dict["clear_repo_cmd"] = "rm -rf {0}".format(code_path + repo_name)
        cmds_dict["git_clone"] = "cd {0} && git clone {1}".format(code_path, stash_addr)
        cmds_dict["git_checkout_cmd"] = "cd {0} && git checkout {1} && git pull".format(code_path + repo_name, branch_name)
        cmds_dict["git_commit_point"] = " git reset --hard {0}".format(commit_point)
        cmds_dict["compile_cmd"] = "./build.sh -{0}".format(parameters)
        return cmds_dict

    @staticmethod
    def __ssh_run_cmd(sys_ip, username, password, cmds):

        client = None
        results = dict()
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(sys_ip, 22, username=username, password=password, compress=True)
            if cmds["git_commit_point"]:
                cmd = cmds["clear_repo_cmd"] + ";" + cmds["git_clone"] + ";" + cmds["git_checkout_cmd"] + ";" + \
                      cmds["git_commit_point"] + ";" + cmds["compile_cmd"]
            else:
                cmd = cmds["clear_repo_cmd"] + ";" + cmds["git_clone"] + ";" + cmds["git_checkout_cmd"] + ";" + \
                      cmds["compile_cmd"]

            print(cmd)

            stdin_compile, stdout_compile, stderr_compile = client.exec_command(command=cmd)
            results["compile_cmd"] = stdout_compile.channel.recv_exit_status()
            results["compile_cmd_detail"] = stdout_compile.readlines()

            return results
        except Exception as e:
            print("Connect virtual machine failed!")
            raise e

        finally:
            client.close()

    def __compile_common(self, is_slam, evn_ip):
        if is_slam:
            cmds = self.__compile_cmds(code_path, "common", stash_core_common, self.branchs['common'])
