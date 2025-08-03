from django.urls import path
from .views import render_home, render_bio, conatact_lists, contact_delete, contact_edit, render_add


urlpatterns = [
        path('', render_home, name="home"),
        path('bio/', render_bio),
        path('contact-list/',conatact_lists, name="contact_list"),
        path('contact-delete/<int:id>', contact_delete, name="contact_delete"),
        path('contact-edit/<int:id>/', contact_edit, name='contact_edit'),
        path('contact-add/', render_add, name='contact_add'),

        # path('contact/', render_contact),
        # path('contact2/', render_contact2)

] 