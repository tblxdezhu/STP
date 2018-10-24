#!/usr/bin/env python
# encoding: utf-8
# @Time    : 10/22/18 5:39 PM
# @Author  : Hong He
# @File    : compile_code.py


'''
define some common function
'''
import paramiko


class Compile_code(object):
    compile_info = {"is_sam": False}

    def __init__(self, *args, **kwarg):

        if kwarg["is_sam"]:
            self.compile_info["is_sam"] = True
            self.compile_info["algorithm_sam"] = kwarg["algorithm_sam"]
        else:
            self.compile_info["is_sam"] = False
            self.compile_info["algorithm_vehicle_offlineslam"] = kwarg["algorithm_vehicle_offlineslam"]

        if kwarg.__contains__("commit_point") and kwarg["commit_point"]:
            self.compile_info["commit_point"] = kwarg["commit_point"]
        else:
            self.compile_info["commit_point"] = ""

        self.compile_info["code_path"] = "/home/roaddb/source/core/"
        self.compile_info["common"] = kwarg["common"]
        self.compile_info["algorithm_common"] = kwarg["algorithm_common"]

        self.compile_info["stash_common"] = "ssh://git@stash.ygomi.com:7999/rc/common.git"
        self.compile_info["stash_algo_common"] = "ssh://git@stash.ygomi.com:7999/rc/algorithm_common.git"
        self.compile_info["stash_algo_vehicle_offlineslam"] = "ssh://git@stash.ygomi.com:7999/rc/algorithm_vehicle_offlineslam.git"
        self.compile_info["stash_algo_sam"] = "ssh://git@stash.ygomi.com:7999/rc/algorithm_sam.git"

    def __compile_cmds__(self, code_path, repo_name, stash_addr, branch_name, commit_point, parameters=""):

        cmds_dict = dict()
        cmds_dict["clear_repo_cmd"] = "rm -rf {0}".format(code_path + repo_name)
        cmds_dict["git_clone"] = "cd {0} && git clone {1}".format(code_path, stash_addr)
        cmds_dict["git_checkout_cmd"] = "cd {0} && git checkout {1} && git pull".format(code_path + repo_name, branch_name)
        cmds_dict["git_commit_point"] = " git reset --hard {0}".format(commit_point)
        cmds_dict["compile_cmd"] = "./build.sh {0}".format(parameters)
        return cmds_dict

    def __ssh_run_cmd__(self, sys_ip, username, password, cmds):

        client = None
        results = dict()
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(sys_ip, 22, username=username, password=password, compress=True)
            cmd = ""

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
            print(results["compile_cmd_detail"])

            return results
        except:
            print("Connect virtual machine failed!")
            raise

        finally:
            client.close()

    def __compile_common(self, evn_ip):

        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "common",
                                     self.compile_info["stash_common"],
                                     self.compile_info["common"], "")

        compile_result = self.__ssh_run_cmd__(evn_ip, "roaddb", "test1234", cmds)

        return compile_result

    def __compile_algo_common(self, is_sam, evn_ip):

        cmds = None
        if not is_sam:
            cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                         "algorithm_common",
                                         self.compile_info["stash_algo_common"],
                                         self.compile_info["algorithm_common"], "",
                                         "-a")

        else:
            cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                         "algorithm_common",
                                         self.compile_info["stash_algo_common"],
                                         self.compile_info["algorithm_common"], "",
                                         "-g")

        compile_result = self.__ssh_run_cmd__(evn_ip, "roaddb", "test1234", cmds)

        return compile_result

    def __compile_algo_offlineslam(self, evn_ip):

        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "algorithm_vehicle_offlineslam",
                                     self.compile_info["stash_algo_vehicle_offlineslam"],
                                     self.compile_info["algorithm_vehicle_offlineslam"],
                                     self.compile_info["commit_point"],
                                     "-aesd")
        # print(cmds)
        compile_result = self.__ssh_run_cmd__(evn_ip, "roaddb", "test1234", cmds)
        return compile_result

    def __compile_algo_sam(self, evn_ip):
        cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "algorithm_sam",
                                     self.compile_info["stash_algo_sam"],
                                     self.compile_info["algorithm_sam"],
                                     self.compile_info["commit_point"],
                                     "-g")
        compile_result = self.__ssh_run_cmd__(evn_ip, "roaddb", "test1234", cmds)
        return compile_result

    def run_compile(self, env_ip):

        result_common = self.__compile_common(env_ip)
        result_algo_common = self.__compile_algo_common(self.compile_info["is_sam"], env_ip)
        result_algo = ""
        print(self.compile_info["is_sam"])
        if not self.compile_info["is_sam"]:
            result_algo = self.__compile_algo_offlineslam(env_ip)
        else:
            result_algo = self.__compile_algo_sam(env_ip)


if __name__ == "__main__":
    obj_compile = Compile_code(common="feature/RDB-28325-offline-slam-developing",
                               algorithm_common="feature/RDB-28325-offline-slam-developing",
                               algorithm_vehicle_offlineslam="feature/RDB-32673-improve-kf-strategy",
                               is_sam=False
                               )
    obj_compile.run_compile("10.69.142.16")
