from django.shortcuts import render

def base_view(request):
	context = {}
	return render(request, "account/manage.html", context)