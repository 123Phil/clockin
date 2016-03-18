"""main URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from clocks import urls as clocks_urls
from account import urls as account_urls
from extras import urls as api_urls

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^account$', include(account_urls, namespace="account")),
	url(r'^api/', include(api_urls, namespace="api")),
	url(r'^', include(clocks_urls, namespace="clocks")),
]
