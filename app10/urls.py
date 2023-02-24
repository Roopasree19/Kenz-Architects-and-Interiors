from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('services/',views.services),
    path('projects/',views.projects),
    path('gallery/',views.gallery),





#################################################################
    path('admin_index/',views.admin_index),
    path('admin_register/',views.admin_register),
    path('admin_login/',views.admin_login),
    path('admin_logout/',views.admin_logout),
]