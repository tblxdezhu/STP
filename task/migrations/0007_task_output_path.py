# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20181016_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='output_path',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
