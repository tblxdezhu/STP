#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 2:52 PM
# @Author  : Zhenxuan Xu
# @File    : test_airflow.py
# @Software: Pycharm professional


from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['zhenxuan.xu@ygomi.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('tutorial', default_args=default_args)

# t1, t2 and t3 are examples of tasks created by instantiating operators
build = BashOperator(
    task_id='build',
    bash_command='echo "build"', dag=dag
)
t1 = BashOperator(
    task_id='SLAM',
    bash_command='echo "SLAM"',
    dag=dag)

t2 = BashOperator(
    task_id='SSA',
    bash_command='echo "SSA"',
    retries=3,
    dag=dag)

# templated_command = """
#     {% for i in range(5) %}
#         echo "{{ ds }}"
#         echo "{{ macros.ds_add(ds, 7)}}"
#         echo "{{ params.my_param }}"
#     {% endfor %}
# """
#
# t3 = BashOperator(
#     task_id='templated',
#     bash_command=templated_command,
#     params={'my_param': 'Parameter I passed in'},
#     dag=dag)

t1.set_upstream(build)
t2.set_upstream(t1)
