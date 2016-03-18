from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.forms import model_to_dict
from django.utils.timezone import now
from .models import Task, Project, Clocked
from .forms import TaskForm, ProjectForm, TaskIdForm

	
#### Rendered Views ###########################################################
def base_view(request):
	context = {}
	u = request.user
	# Show the splash if not logged in:
	if not u.is_authenticated():
		return render(request, "clocks/splash.html", context)
	# Show the clocked-in page if clocked in:
	task_fields = ['name', 'task_id', 'order', 'color', 'seconds']
	project_fields = ['name', 'project_id', 'color', 'order']
	c = Clocked.objects.filter(username=u.username).first()
	if c:
		delta = now() - c.clock_time
		elapsed = int(delta.total_seconds())
		context["elapsed"] = elapsed
		try:
			t = Task.objects.get(username=u.username, task_id=c.task_id)
			context["task"] = model_to_dict(t, fields=task_fields)
			#TODO: show other tasks/projects...
			return render(request, "clocks/clocked.html", context)
		except Task.DoesNotExist as e:
			#TODO ??
			pass
	# Show the tasks page when logged in and clocked out:
	context["task_form"] = TaskForm()
	context["project_form"] = ProjectForm()
	context["task_id_form"] = TaskIdForm()
	project_entries = Project.objects.filter(username=u.username)
	task_entries = Task.objects.filter(username=u.username, project=None)
	tasks = [model_to_dict(t, fields=task_fields) for t in task_entries]
	for task in tasks:
		task["time_str"] = time_string(task["seconds"])
	for project in project_entries:
		p = model_to_dict(project, fields=project_fields)
		p_tasks = Task.objects.filter(username=u.username,
			project=project).order_by('order')
		task_entries = Task.objects.filter(username=u.username, project=project)
		p["tasks"] = [model_to_dict(t, fields=task_fields) for t in task_entries]
		for task in p["tasks"]:
			task["time_str"] = time_string(task["seconds"])
		p["is_project"] = True
		tasks.append(p)
	tasks.sort(key=lambda x: x["order"])
	context["tasks"] = tasks
	return render(request, "clocks/tasks.html", context)


#### utils ####################################################################
def get_form(request, FormClass):
	if request.method != 'POST':
		raise Http404('Invalid request.')
	f = FormClass(request.POST)
	if not f.is_valid():
		raise Http404('Invalid form.')
	return f

def get_new_task_id(username):
	previous_tasks = Task.objects.filter(username=username)
	if previous_tasks:
		return max(t.task_id for t in previous_tasks) + 1
	else:
		return 1

def get_new_task_order(username, project):
	previous_tasks = Task.objects.filter(username=username, project=project)
	ids = [t.order for t in previous_tasks]
	if not project:
		ids += [p.order for p in Project.objects.all()]
	if ids:
		return max(ids) + 1
	else:
		return 1

def time_string(seconds):
	h = int(seconds // 3600)
	m = int(seconds // 60 % 60)
	s = int(seconds % 60)
	time_str = "<b>{0:02}</b> M <b>{1:02}</b> S".format(m,s)
	if h != 0:
		time_str = "<b>{}</b> H ".format(h) + time_str
	return time_str


#### New Task/Project #########################################################
@login_required
def new_task(request):
	task_form = get_form(request, TaskForm)
	u = request.user
	n = task_form.cleaned_data["name"]
	c = task_form.cleaned_data["color"]
	p = task_form.cleaned_data["project_id"]
	p = Project.objects.filter(project_id=p).first()
	task_id = get_new_task_id(u.username)
	order = get_new_task_order(u.username, p)
	Task.objects.create(name=n, username=u.username, task_id=task_id,
			order=order, color=c, project=p, seconds=0)
	return redirect('/')


@login_required
def new_project(request):
	p_form = get_form(request, ProjectForm)
	u = request.user
	n = p_form.cleaned_data["p_name"]
	c = p_form.cleaned_data["p_color"]
	p_id = 1
	p_ids = [p.project_id for p in Project.objects.all()]
	if p_ids:
		p_id = max(p_ids) + 1
	order = get_new_task_order(u.username, None)
	Project.objects.create(name=n, username=u.username, project_id=p_id,
			order=order, color=c)
	return redirect('/')


#### Clock in/out #############################################################
@login_required
def clock_in(request):
	id_form = get_form(request, TaskIdForm)
	t = id_form.cleaned_data["task_id"]
	Clocked.objects.create(username=request.user.username, task_id=t)
	return redirect('/')


@login_required
def clock_out(request):
	u = request.user
	try:
		c = Clocked.objects.get(username=u.username)
		delta = now() - c.clock_time
		elapsed = delta.total_seconds()
		Task.objects.filter(username=u.username,
			task_id=c.task_id).update(seconds=F('seconds') + elapsed)
		c.delete()
	except Clocked.DoesNotExist:
		pass
	except:
		raise Http404('Database error.')
	return redirect('/')


#### Edit/delete task/project #################################################
def reorder(request): 
	pass

def edit_task(request):
	pass

def edit_project(request):
	pass

def kill_task(request):
	pass

def kill_project(request):
	pass







