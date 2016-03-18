from django import forms

class TaskForm(forms.Form):
	name = forms.CharField()
	color = forms.CharField()
	project_id = forms.IntegerField()

class TaskIdForm(forms.Form):
	task_id = forms.IntegerField()

class ProjectForm(forms.Form):
	p_name = forms.CharField()
	p_color = forms.CharField(max_length=6)

class OrderForm(forms.Form):
	order = forms.CharField()
	