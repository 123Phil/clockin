"""clocks app url config"""

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.base_view, name='base_view'),
	url(r'^/$', views.base_view, name='base_view'),
	url(r'^clockout$', views.clock_out, name='clock_out'),
	url(r'^clockin$', views.clock_in, name='clock_in'),
	url(r'^newtask$', views.new_task, name='new_task'),
	url(r'^newproject$', views.new_project, name='new_project'),
	url(r'^edittask$', views.edit_task, name='edit_task'),
	url(r'^killtask$', views.kill_task, name='kill_task'),
	url(r'^killproject$', views.kill_project, name='kill_project'),
]
