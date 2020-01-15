from django.shortcuts import render
from home.models import Project


def home_screen_view(request):
	context = {}
	projects = Project.objects.all()
	context['projects'] = projects

	return render(request, 'home.html', context)