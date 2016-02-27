# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('project_id', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('task_id', models.SmallIntegerField()),
                ('seconds', models.IntegerField()),
                ('project', models.ForeignKey(to='clocks.Project')),
            ],
        ),
    ]
