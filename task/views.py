from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Task
from task.tasks import print_task


# Create your views here.
@login_required
def test(request):
    return render(request, 'run_slam_ssa_test.html', {'username': request.user.username, 'if_test_active': 'active'})


# @login_required
# def submitted(request):
#     if 'select_mode' in request.POST:
#         print(request.POST['select_mode'])
#         print(request.POST.getlist('check_box_list'))
#         print(request.POST['common'])
#         print(request.POST['algo_common'])
#         return render(request, 'run_slam_ssa_test.html',
#                       {'username': request.user.username, 'if_test_active': 'active'})
#

@login_required
def submitted(request):
    branchs = {'common': request.POST['common'], 'algo_common': request.POST['algo_common']}
    task = Task(tester=request.user, mode=request.POST['select_mode'], branch=branchs, area=request.POST.getlist('check_box_list'))
    task.save()
    print_task.delay("xu")
    return render(request, 'submitted.html', {'task': task})
