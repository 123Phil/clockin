# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color',
            field=models.CharField(default='000000', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
