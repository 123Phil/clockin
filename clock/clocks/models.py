from django.db import models


class Project(models.Model):
	name = models.CharField(max_length=80)
	username = models.CharField(max_length=80)
	project_id = models.SmallIntegerField()

	def __str__(self):
		return self.name

class Task(models.Model):
	name = models.CharField(max_length=80)
	username = models.CharField(max_length=80)
	task_id = models.SmallIntegerField()
	project = models.ForeignKey(Project)
	seconds = models.IntegerField()

	def __str__(self):
		return self.name
