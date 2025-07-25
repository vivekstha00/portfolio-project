from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def render_project(request):
    template = 'project.html'
    return render(request, template)

def render_ProDetails(request):
    template = 'project-details.html'
    return render(request, template)
