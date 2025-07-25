from django.urls import path 
from .views import *

urlpatterns = [
    path('projects/', render_project),
    path('Pro_details/', render_ProDetails)
]