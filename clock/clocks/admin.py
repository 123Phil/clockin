from django.contrib import admin
from .models import Task, Project, Clocked

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Clocked)

