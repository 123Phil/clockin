"""clocks app url config"""

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.base_view, name='base_view'),
	url(r'^clockout$', views.clock_out, name='clock_out'),
	url(r'^new_task$', views.new_task, name='new_task'),
	url(r'^new_project$', views.new_project, name='new_project'),
	url(r'^edit_task$', views.edit_task, name='edit_task'),
	url(r'^kill_task$', views.kill_task, name='kill_task'),
	url(r'^kill_project$', views.kill_project, name='kill_project'),
]
