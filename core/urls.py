from django.urls import path
from .views import render_home, render_bio
# from core.view import render_home

urlpatterns = [
        path('', render_home),
        path('bio/', render_bio)
] 