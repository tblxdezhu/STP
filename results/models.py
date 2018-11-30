from django.db import models


# from task.models import Task


# Create your models here.

class Results(models.Model):
    task_id = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    mode = models.CharField(max_length=10)
    rtv_name = models.CharField(max_length=50)
    slam_len = models.CharField(max_length=10)
    gps_len = models.CharField(max_length=10)
    kfs = models.CharField(max_length=10)
    rtv_frames = models.CharField(max_length=10)
    mps = models.CharField(max_length=10)
    avg_track_len_mp = models.CharField(max_length=10)
    weak_rate = models.CharField(max_length=10)
    mp_kf = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    efficiency = models.CharField(max_length=10)

    rmse = models.CharField(max_length=10, null=True)

    class Meta:
        ordering = ('-task_id',)

    def __str__(self):
        return "{}_{}_{}".format(self.task_id, self.mode, self.rtv_name)
