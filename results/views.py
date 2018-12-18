from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import os


# Create your views here.

@login_required
def analyse_data(request):
    return render(request, 'analyse_data.html')


@login_required
def get_json_data(request):
    print("get json data")
    print(os.getcwd())
    with open("{}/static/jsons/cityData.json".format(os.getcwd()), 'r') as f:
        json_data = json.load(f)
    return JsonResponse(json_data, safe=False)
