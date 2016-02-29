# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clocks', '0003_auto_20160227_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clocked',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=80)),
                ('task_id', models.SmallIntegerField()),
                ('clock_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
