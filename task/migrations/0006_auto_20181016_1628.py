# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_task_celery_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='celery_id',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
