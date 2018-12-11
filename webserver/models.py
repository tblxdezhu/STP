from django.db import models


# Create your models here.

class Machine(models.Model):
    machine_id = models.CharField(max_length=50)
    process_num = models.CharField(max_length=10)
    code_path = models.CharField(max_length=100)
    output_path = models.CharField(max_length=100)

    def __str__(self):
        return self.machine_id


class Data(models.Model):
    area = models.CharField(max_length=20)
    data_path = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    gps_skeleton_path = models.CharField(max_length=100, blank=True)
    road_skeleton_path = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.area
