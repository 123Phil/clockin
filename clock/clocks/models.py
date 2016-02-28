from django.db import models


class Project(models.Model):
	name = models.CharField(max_length=80)
	username = models.CharField(max_length=80)
	project_id = models.SmallIntegerField()
	color = models.CharField(max_length=6)
	order = models.SmallIntegerField()

	def __str__(self):
		return self.name

class Task(models.Model):
	name = models.CharField(max_length=80)
	username = models.CharField(max_length=80)
	color = models.CharField(max_length=6)
	order = models.SmallIntegerField()
	task_id = models.SmallIntegerField()
	project = models.ForeignKey(Project, null=True)
	seconds = models.IntegerField()

	def __str__(self):
		return self.name
