from django.db import models


# Create your models here.
class DataManager(models.Manager):
    def all_areas(self):
        return [str(i[0]) for i in self.values_list('area')]


class Machine(models.Model):
    ip = models.CharField(max_length=20, default="127.0.0.1")
    username = models.CharField(max_length=50, default="roaddb")
    password = models.CharField(max_length=50, default="test1234")
    port = models.IntegerField(default=22)
    machine_id = models.CharField(max_length=50)
    process_num = models.IntegerField()
    code_path = models.CharField(max_length=100, default="/home/roaddb/source/core")
    output_path = models.CharField(max_length=100)
    data_path = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Data(models.Model):
    area = models.CharField(max_length=20)
    data_path = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    gps_skeleton_path = models.CharField(max_length=100, blank=True)
    road_skeleton_path = models.CharField(max_length=100, blank=True)
    tag = models.CharField(max_length=20, default="tmp")
    data_type = models.CharField(max_length=20, default=".img")
    objects = DataManager()

    def __str__(self):
        return self.area
