
# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def large_data(request):
    return render(request, "large.html", {'if_large_active': 'active'})


@login_required
def mini_data(request):
    return render(request, "mini.html", {'if_mini_active': 'active'})


@login_required
def error_data(request):
    return render(request, "error.html", {'if_error_active': 'active'})
