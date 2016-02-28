"""main URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from clocks import urls as clocks_urls
from account import urls as account_urls
from clocks import views as clocks_views

urlpatterns = [
	url(r'^$', clocks_views.base_view, name='base_view'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^account$', include(account_urls, namespace="account")),
	url(r'^clocks/', include(clocks_urls, namespace="clocks")),
]
