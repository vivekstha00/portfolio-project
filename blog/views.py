from django.shortcuts import render
from django.http import HttpResponse

def render_blog(request):
    template = 'blog.html'
    return render(request, template)

def render_details(request):
    template = 'blogDetails.html'
    return render(request, template)

# Create your views here.
