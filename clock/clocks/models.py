from django.db import models


class Project(models.Model):
	name = models.CharField(max_length=80)
	username = models.CharField(max_length=80)
	project_id = models.IntegerField()
	color = models.CharField(max_length=6)
	order = models.IntegerField()

	def __str__(self):
		return " ".join([self.username, self.name])

class Task(models.Model):
	name = models.CharField(max_length=80)
	username = models.CharField(max_length=80)
	color = models.CharField(max_length=6)
	order = models.IntegerField()
	task_id = models.IntegerField()
	project = models.ForeignKey(Project, null=True)
	seconds = models.IntegerField()

	def __str__(self):
		project_name = ''
		if self.project:
			project_name = ' - Project: ' + self.project.name
		return " ".join([self.username, self.name, project_name])

class Clocked(models.Model):
	username = models.CharField(max_length=80)
	task_id = models.IntegerField()
	clock_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return " ".join([self.username, "- task", str(self.task_id),
			"- start time:", self.clock_time.strftime("%x %X")])
