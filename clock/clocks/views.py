from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import F
from .models import Task, Project


#### Rendered Views ###########################################################
def base_view(request):
	context = {}
	u = request.user
	if u.is_authenticated():
		context["tasks"] = Task.objects.filter(username=u.username)
		return render(request, "clocks/tasks.html", context)
	else:
		return render(request, "clocks/splash.html", context)


#### API calls ################################################################
def clock_out(request):
	if not verify(request):
		return Http404('Invalid request.')
	u = request.user
	task_id = request.POST["id"]
	seconds = request.POST["seconds"]
	try:
		task_entry = Task.objects.get(username=u.username,
			task_id=task_id).update(seconds=F('seconds') + seconds)
	except Task.DoesNotExist:
		return Http404('Database error.')
	return HttpResponse('success')


def new_task(request):
	if not verify(request):
		return Http404('Invalid request.')
	u = request.user
	task_id = 1
	try:
		previous_tasks = Task.objects.filter(username=u.username)
		if previous_tasks:
			task_id = max(t.task_id for t in previous_tasks) + 1
		n = request.POST["name"]
		p = request.POST["project"]
		new_task = Task(name=n, username=u.username, task_id=task_id,
			project=p, seconds=0)
		new_task.save()
		return HttpResponse('success')
	except:
		return Http404('Unable to create task.')

def new_project(request):
	pass

def edit_task(request):
	pass

def edit_project(request):
	pass

def kill_task(request):
	pass

def kill_project(request):
	pass


#### Helper functions #########################################################
def verify(request):
	if not request.user.is_authenticated():
		return False
	elif request.method != 'POST':
		return False
	else:
		return True





