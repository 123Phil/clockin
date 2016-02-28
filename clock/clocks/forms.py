from django import forms

class TaskForm(forms.Form):
	name = forms.CharField()
	color = forms.CharField()
	project = forms.CharField()


class ProjectForm(forms.Form):
	name = forms.CharField()
	color = forms.CharField(max_length=6)
