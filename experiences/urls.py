from django.urls import path 
from .views import experiences, experience_details

urlpatterns = [
    path('experiences/', experiences),
    path('experi_details/', experience_details)
]