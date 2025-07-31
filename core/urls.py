from django.urls import path
from .views import render_home, render_bio, conatact_lists, contact_delete
# from core.view import render_home

urlpatterns = [
        path('', render_home),
        path('bio/', render_bio),
        path('contact-list/',conatact_lists, name="contact_list"),
        path('contact-delete/<int:id>', contact_delete, name="contact_delete")
        # path('contact/', render_contact),
        # path('contact2/', render_contact2)

] 