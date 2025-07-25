from django.urls import path
from .views import render_blog, render_details


urlpatterns = [
        path('blog/', render_blog),
        path('details/', render_details)
]