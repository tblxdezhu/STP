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

    compile_info=dict()

    def __init__(self,task_id,common="master",algo_common="master",algo_vehicle_offlineslam="master",
                 common_sam="master",algo_common_sam="master",algo_sam="master",algo_sam_commit="",
                 algo_offlineSLAM_commit=""
                 ):
        self.compile_info["code_path"]= "/home/roaddb/test_code/"
        self.compile_info["common"] = common
        self.compile_info["algo_common"] = algo_common
        self.compile_info["algo_vehicle_offlineslam"] = algo_vehicle_offlineslam
        self.compile_info["common-sam"] = common_sam
        self.compile_info["algo_common-sam"] = algo_common_sam
        self.compile_info["algo_sam"] = algo_sam
        self.compile_info["algo_sam_commit"]=algo_sam_commit
        self.compile_info["algo_offlineSLAM_commit"]=algo_offlineSLAM_commit
        self.compile_info["task_id"]=task_id

        self.compile_info["stash_common"]="ssh://git@stash.ygomi.com:7999/rc/common.git"
        self.compile_info["stash_algo_common"]="ssh://git@stash.ygomi.com:7999/rc/algorithm_common.git"
        self.compile_info["stash_algo_vehicle_offlineslam"]="ssh://git@stash.ygomi.com:7999/rc/algorithm_vehicle_offlineslam.git"
        self.compile_info["stash_algo_sam"]="ssh://git@stash.ygomi.com:7999/rc/algorithm_sam.git"

    def __compile_cmds__(self,code_path,repo_name,stash_addr,branch_name,commit_point,parameters=""):

        cmds_dict=dict()
        cmds_dict["clear_repo_cmd"]="rm -rf {0}".format(code_path+repo_name)
        cmds_dict["git_clone"]="cd {0} && git clone {1}".format(code_path,stash_addr)
        cmds_dict["git_checkout_cmd"]="cd {0} && git checkout {1} && git pull".format(code_path+repo_name,branch_name)
        cmds_dict["git_commit_point"]=" git reset --hard {0}".format(commit_point)
        cmds_dict["compile_cmd"]="./build.sh -{0}".format(parameters)
        return cmds_dict

    def __ssh_run_cmd__(self,sys_ip,username,password,cmds):

        client=None
        results=dict()
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(sys_ip, 22, username=username, password=password, compress=True)
            #print(sys_ip, 22, username, password)
            cmd=""
            if cmds["git_commit_point"]:
                cmd=cmds["clear_repo_cmd"]+";"+cmds["git_clone"]+";"+cmds["git_checkout_cmd"]+";"+\
                    cmds["git_commit_point"]+";"+cmds["compile_cmd"]
            else:
                cmd=cmds["clear_repo_cmd"]+";"+cmds["git_clone"]+";"+cmds["git_checkout_cmd"]+";"+\
                    cmds["compile_cmd"]

            print(cmd)
            # stdin_clear,stdout_clear,stderr_clear=client.exec_command(command=cmds["clear_repo_cmd"])
            # results["clear_repo_cmd"]=stdout_clear
            # results["sdterr"]=stderr_clear
            #
            # stdin_clone, stdout_clone, stderr_clone = client.exec_command(command=cmds["git_clone"])
            # results["git_clone"] = stdout_clone
            # results["sdterr"]+=stderr_clone
            #
            # stdin_checkout, stdout_checkout, stderr_checkout = client.exec_command(command=cmds["git_checkout_cmd"])
            # results["git_checkout_cmd"] = stdout_checkout
            # results["sdterr"] += stderr_checkout

            stdin_compile, stdout_compile, stderr_compile = client.exec_command(command=cmd)
            results["compile_cmd"] = stdout_compile.channel.recv_exit_status()
            results["compile_cmd_detail"] = stdout_compile.readlines()

            return results
        except:
            print("Connect virtual machine failed!")
            raise

        finally:
            client.close()

    def __compile_common(self,is_slam,evn_ip):

        cmds=None
        if is_slam:
            cmds=self.__compile_cmds__(self.compile_info["code_path"],
                              "common",
                              self.compile_info["stash_common"],
                              self.compile_info["common"],"")
        else:
            cmds = self.__compile_cmds__(self.compile_info["code_path"],
                                     "common",
                                     self.compile_info["stash_common"],
                                     self.compile_info["common-sam"],"")

        compile_result=self.__ssh_run_cmd__(evn_ip,"roaddb","test1234",cmds)

        return compile_result

    def __compile_algo_common(self,is_slam,evn_ip):

        cmds=None
        if is_slam:
            cmds=self.__compile_cmds__(self.compile_info["code_path"],
                                       "algorithm_common",
                                       self.compile_info["stash_algo_common"],
                                       self.compile_info["algo_common"],"",
                                       "g")

        else:
            cmds=self.__compile_cmds__(self.compile_info["code_path"],
                                       "algorithm_common",
                                       self.compile_info["stash_algo_common"],
                                       self.compile_info["algo_common-sam"],"",
                                       "g")

        compile_result=self.__ssh_run_cmd__(evn_ip,"roaddb","test1234",cmds)

        return compile_result

    def __compile_algo_offlineslam(self,evn_ip):

        cmds=self.__compile_cmds__(self.compile_info["code_path"],
                                   "algorithm_vehicle_offlineslam",
                                   self.compile_info["stash_algo_vehicle_offlineslam"],
                                   self.compile_info["algo_vehicle_offlineslam"],
                                   self.compile_info["algo_offlineSLAM_commit"],
                                   "aes")
        #print(cmds)
        compile_result=self.__ssh_run_cmd__(evn_ip,"roaddb","test1234",cmds)
        return compile_result

    def __compile_algo_sam(self,evn_ip):
        cmds=self.__compile_cmds__(self.compile_info["code_path"],
                                   "algorithm_sam",
                                   self.compile_info["stash_algo_sam"],
                                   self.compile_info["algo_common-sam"],
                                   self.compile_info["algo_sam_commit"],
                                    "g")
        compile_result=self.__ssh_run_cmd__(evn_ip,"roaddb","test1234",cmds)
        return compile_result

    def run_compile(self,is_slam,env_ip):


        result_common=self.__compile_common(is_slam,env_ip)
        print(result_common)
        # for item in result_common:
        #     print(item)
        result_algo_common=self.__compile_algo_common(is_slam,env_ip)
        print(result_algo_common)
        result_algo=""
        if is_slam:
            result_algo=self.__compile_algo_offlineslam(env_ip)
        else:
            result_algo=self.__compile_algo_sam(env_ip)

        print(result_algo)

if __name__=="__main__":


    obj_compile=Compile_code(1,common="feature/RDB-28325-offline-slam-developing",
                             algo_common="feature/RDB-28325-offline-slam-developing",
                             algo_vehicle_offlineslam="feature/RDB-28325-offline-slam-developing"
                             )
    obj_compile.run_compile(False,"10.69.142.16")
