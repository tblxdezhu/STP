# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import random
import os
import subprocess
import paramiko


# Create your views here.

@login_required
def lab_info(requst):
    return render(requst, "lab.html")


def lab_cpu(request):
    result, cpu_used_per_min = None, None

    if request.is_ajax() and request.GET.get("virtualCpu") == "16":
        result, cpu_used_per_min = subprocess.getstatusoutput(
            "snmpwalk -v 2c -c roaddb 10.69.142.16 .1.3.6.1.4.1.2021.11.9.0")
    else:
        result, cpu_used_per_min = subprocess.getstatusoutput(
            "snmpwalk -v 2c -c roaddb 10.69.142.17 .1.3.6.1.4.1.2021.11.9.0")

    print(cpu_used_per_min)
    return JsonResponse({"info": float(eval(cpu_used_per_min.split(":")[-1]))})


def lab_used_memory(request):
    use_percentage = 0
    free_memory_used = 0

    if request.GET.get("virtualMemo") == "16":

        total_result, total_memory_used = subprocess.getstatusoutput(
            "snmpwalk -v 2c -c roaddb 10.69.142.16 .1.3.6.1.4.1.2021.4.5.0")
        free_result, free_memory_used = subprocess.getstatusoutput(
            "snmpwalk -v 2c -c roaddb 10.69.142.16 .1.3.6.1.4.1.2021.4.11.0")
        use_percentage = round(
            (int(eval(free_memory_used.split(":")[-1])) / int(eval(total_memory_used.split(":")[-1]))) * 100, 2)

    else:
        total_result, total_memory_used = subprocess.getstatusoutput(
            "snmpwalk -v 2c -c roaddb 10.69.142.17 .1.3.6.1.4.1.2021.4.5.0")
        free_result, free_memory_used = subprocess.getstatusoutput(
            "snmpwalk -v 2c -c roaddb 10.69.142.17 .1.3.6.1.4.1.2021.4.11.0")
        use_percentage = round(
            (int(eval(free_memory_used.split(":")[-1])) / int(eval(total_memory_used.split(":")[-1]))) * 100, 2)

    return JsonResponse({"usedMemoPercent": 100 - use_percentage})


def lab_cpu_memory(request):
    core_info = ""
    memo_info = ""
    if request.GET.get("virtualStaticInfo") == "16":
        total_mem_result, memo_info = subprocess.getstatusoutput(
            "snmpwalk -v 2c -c roaddb 10.69.142.16 .1.3.6.1.4.1.2021.4.5.0")
    else:
        total_mem_result, memo_info = subprocess.getstatusoutput(
            "snmpwalk -v 2c -c roaddb 10.69.142.16 .1.3.6.1.4.1.2021.4.5.0")
    memo_size_MB = int(int(eval(memo_info.split(":")[-1])) / 1024)

    return JsonResponse({"memorySize": "Memory Size:" + str(memo_size_MB) + "MB"})
