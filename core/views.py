from django.shortcuts import render
from .models import Bio, Statistics, Skills
from projects.models import Resume


def render_home(request):
    bio = Bio.objects.first()
    stat = Statistics.objects.all()
    skills = Skills.objects.all()
    resume = Resume.objects.all()

    name = bio.name
    title = bio.titles
    email = bio.email

    template = 'index.html'
    context ={
        'bio': bio, 
        'statistics' : stat,
        'skills': skills,
        'resume': resume,
    }

    return render(request, template, context)


# Create your views here.

def render_bio(request):
    
    template = 'bio.html'
    return render(request, template)