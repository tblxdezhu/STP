from django.db import models


# from task.models import Task


# Create your models here.

class ResultsManager(models.Manager):
    def show_task_id(self):
        return [str(i[0]) for i in self.order_by('task_id').values_list('task_id').distinct()]

    def total(self, task_id, keyword):
        return sum([float(i[0]) for i in self.filter(task_id=task_id).values_list(keyword)])

    def area_total(self, task_id, keyword, area):
        return sum([float(i[0]) for i in self.filter(task_id=task_id).filter(area=area).values_list(keyword)])

    def show_data_of_area(self, task_id, keyword, area):
        return [str(i[0]) for i in self.filter(task_id=task_id).filter(area=area).order_by('id').values_list(keyword)]


class Results(models.Model):
    task_id = models.IntegerField()
    area = models.CharField(max_length=30)
    mode = models.CharField(max_length=10)
    rtv_name = models.CharField(max_length=200)
    slam_len = models.CharField(max_length=20)
    gps_len = models.CharField(max_length=20)
    kfs = models.CharField(max_length=10)
    rtv_frames = models.CharField(max_length=10)
    mps = models.CharField(max_length=10)
    avg_track_len_mp = models.CharField(max_length=10)
    weak_rate = models.CharField(max_length=10)
    mp_kf = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    efficiency = models.CharField(max_length=10)

    rmse = models.CharField(max_length=10, null=True)

    objects = ResultsManager()

    class Meta:
        ordering = ('-task_id',)

    def __str__(self):
        return "{}_{}_{}".format(self.task_id, self.mode, self.rtv_name)


class Overview(models.Model):
    task_id = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    rmse = models.CharField(max_length=10, null=True)
    time = models.CharField(max_length=10)
    coverage = models.CharField(max_length=10)

    class Meta:
        ordering = ('-task_id',)

    def __str__(self):
        return "{}".format(self.task_id)
