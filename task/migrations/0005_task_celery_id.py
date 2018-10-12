# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20181010_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='celery_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
