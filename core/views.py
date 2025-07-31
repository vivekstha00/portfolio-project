from django.shortcuts import render, redirect
from .models import Bio, Statistics, Skills
from projects.models import Resume
from .forms import *



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


def conatact_lists(request):
    conatact_lists = EnquiryForm.objects.all()
    context = {
        'contact_lists': conatact_lists
    }
    return render (request, 'contact/list.html', context)

def contact_delete(request, id):
    if request.method == "POST":
        enquiry = EnquiryForm.objects.get(id=id)
        enquiry.delete()
        return redirect('contact_list')
    return render(request, 'contact/delete.html')


# def render_contact(request):
#     if request.method == "POST":
#         input_name = request.POST['name']
#         input_email = request.POST['email']
#         input_subject = request.POST['subject']
#         input_message = request.POST['message']
#         EnquiryForm.objects.create(
#             name = input_name,
#             email = input_email,
#             subject = input_subject,
#             message = input_message
#         )
#     template = 'contact.html'
#     return render(request, template)

# def render_contact2(request):
#     if request.method =="POST":
#         form = UserEnquiryForm(request.POST)
#         if form.is_valid():
#             name= form.cleaned_data['name']
#             email= form.cleaned_data['email']
#             subject= form.cleaned_data['subject']
#             message= form.cleaned_data['message']

#     context = {
#         'enquiry_forms': UserEnquiryForm()
#     }

#     template = 'contact2.html'
#     return render(request, template)