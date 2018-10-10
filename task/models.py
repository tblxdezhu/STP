from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Task(models.Model):
    tester = models.ForeignKey(User, related_name="tasks")
    created = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=200, db_index=True)
    mode = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{}:{}".format(self.id, self.tester)



