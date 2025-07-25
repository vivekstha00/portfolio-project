from django.shortcuts import render
from django.http import HttpResponse

def experiences(request):
    template = 'exper.html'
    return render(request, template)

def experience_details(request):
    template = 'expDetails.html'
    return render(request, template)

# Create your views here.
