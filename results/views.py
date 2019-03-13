from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import os
from task.models import Task
from task.views import draw_line


# Create your views here.

@login_required
def analyse_data(request):
    tasks = Task.objects.all()
    return render(request, 'analyse_data.html', {'tasks': tasks})


@login_required
def get_json_data(request):
    print("get json data")
    print(os.getcwd())
    with open("{}/static/jsons/cityData.json".format(os.getcwd()), 'r') as f:
        json_data = json.load(f)
    return JsonResponse(json_data, safe=False)


@login_required
def get_charts_from_db(request, info):
    print("info", info)
    charts = {}
    print(info.split("_")[-1].rstrip("/").split(","))
    for task in info.split("_")[-1].split(","):
        charts[task] = draw_line(int(task))
        page = draw_line(int(task))
        myechart = page.render_embed()
        print(myechart)
        script_list = page.get_js_dependencies()
    return JsonResponse({'charts': myechart})
