from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Task, Project
from .forms import TaskForm, ProjectForm


#### Rendered Views ###########################################################
def base_view(request, invalid_t_form=False, invalid_p_form=False):
	context = {}
	u = request.user
	if not u.is_authenticated():
		return render(request, "clocks/splash.html", context)
	if invalid_t_form:
		task_form = TaskForm(request.POST)
	else:
		task_form = TaskForm()
	if invalid_p_form:
		project_form = ProjectForm(request.POST)
	else:
		project_form = ProjectForm()
	context["seconds"] = 0
	context["task_form"] = task_form
	context["project_form"] = project_form
	context["bad_t_form"] = invalid_t_form
	context["bad_p_form"] = invalid_p_form
	context["tasks"] = Task.objects.filter(username=u.username)
	return render(request, "clocks/tasks.html", context)


#### Form submit & redirect ?? ################################################
@login_required
def new_task(request):
	if request.method != 'POST':
		raise Http404('Invalid request.')
	u = request.user
	task_id = 1
	order = 1
	previous_tasks = Task.objects.filter(username=u.username)
	if previous_tasks:
		#TODO: DB F query for these ??
		task_id = max(t.task_id for t in previous_tasks) + 1
		order = max(t.order for t in previous_tasks) + 1
	task_form = TaskForm(request.POST)
	if not task_form.is_valid():
		return base_view(request, invalid_t_form=True)
	n = task_form.cleaned_data["name"]
	c = task_form.cleaned_data["color"]
	p = task_form.cleaned_data["project"]
	if p:
		try:
			p = Project.objects.get(name=p)
		except:
			p = None
	else:
		p = None
	try:
		new_task = Task(name=n, username=u.username, task_id=task_id,
			order=order, color=c, project=p, seconds=0)
		new_task.save()
	except Exception as e:
		raise Http404(e)
	return redirect('/')



@login_required
def new_project(request):
	pass


#### API calls ################################################################
@login_required
def clock_out(request):
	if not request.method != 'POST':
		raise Http404('Invalid request.')
	u = request.user
	task_id = request.POST["id"]
	seconds = request.POST["seconds"]
	try:
		task_entry = Task.objects.get(username=u.username,
			task_id=task_id).update(seconds=F('seconds') + seconds)
	except Task.DoesNotExist:
		raise Http404('Database error.')
	return HttpResponse('success')

def edit_task(request):
	pass

def edit_project(request):
	pass

def kill_task(request):
	pass

def kill_project(request):
	pass







