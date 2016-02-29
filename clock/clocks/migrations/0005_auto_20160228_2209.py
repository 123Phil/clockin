# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clocks', '0004_clocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clocked',
            name='task_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.IntegerField(),
        ),
    ]
