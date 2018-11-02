from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.template import Template, Context
from task.models import Task


# Create your views here.

def login(request):
    if request.method == 'GET':
        uf = UserForm()
        return render(request, 'login.html', {'forms': uf})
    else:
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = request.POST.get("username", '')
            password = request.POST.get("password", '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                c = Context({'username': username, 'if_index_active': 'active'})
                return HttpResponseRedirect("/dashboard")
            else:
                return render(request, 'login.html', {'forms': uf, 'password_is_wrong': True})
        else:
            return render(request, 'login.html', {'forms': uf, 'username_is_wrong': True})


@login_required
def index(request):
    return render(request, 'dashboard.html')


@login_required
def elements(request):
    return render(request, 'elements.html')


def forgot(request):
    if request.method == 'GET':
        uf = UserForm()
        return render(request, 'login.html', {'forms': uf, 'forgot_passwd': True})


def test(request):
    return render(request, 'test.html')


def test_login(request):
    return render(request, 'login.html')


@login_required
def coming(request):
    return render(request, 'coming_soon.html')


@login_required
def basic_use(request):
    return render(request, 'basic_use.html')
