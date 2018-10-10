from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Task
from task.tasks import print_task
from django.core.urlresolvers import reverse


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
    branchs = {'common': request.POST['common'], 'algo_common': request.POST['algo_common'], 'algo_vehicle_offlineslam': request.POST['algo_vehicle_offlineslam'],
               'common-sam': request.POST['common-sam'], 'algo_common-sam': request.POST['algo_common-sam']}
    task = Task(tester=request.user, mode=request.POST['select_mode'], branch=branchs, area=request.POST.getlist('check_box_list'))
    task.save()
    result = print_task.delay("xu")
    print(result.task_id)
    # while True:
    #     print(result.status)
    #     if result.ready():
    #         break
    # print(result.status)
    # return render(request, 'submitted.html', {'task': task})
    return HttpResponseRedirect(reverse('task_id', kwargs={'task_id': task.id}))


@login_required
def task_process(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'submitted.html', {'task': task, 'branchs': eval(task.branch)})


@login_required
def dashboard(request):
    print(request.user)
    tasks = Task.objects.all()[0:5]
    my_tasks = Task.objects.filter(tester=request.user)[0:5]
    return render(request, 'dashboard.html', {'tasks': tasks, 'my_tasks': my_tasks})


@login_required
def all_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'all_tasks.html', {'tasks': tasks})


@login_required
def all_my_tasks(request):
    tasks = Task.objects.filter(tester=request.user)
    return render(request, 'all_my_tasks.html', {'tasks': tasks})
