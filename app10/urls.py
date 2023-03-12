from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('services/',views.services),
    path('projects/',views.projects),
    path('gallery/',views.gallery),
    path('servicespage/',views.servicespage),
    path('get/',views.get),
    path('contactus/',views.contactus),
    path('index2/',views.index2),







#################################################################
    path('admin_index/',views.admin_index),
    path('admin_register/',views.admin_register),
    path('admin_login/',views.admin_login),
    path('admin_logout/',views.admin_logout),
    path('admin_service/',views.admin_service),
    path('admin_servtb/',views.admin_servtb),
    path('admin_servupd/',views.admin_servupd),
    path('admin_servdlt/',views.admin_servdlt),
    path('admin_projects/',views.admin_projects),
    path('admin_protb/',views.admin_protb),
    path('admin_projupd/',views.admin_projupd),
    path('admin_projdlt/',views.admin_projdlt),
    path('admin_gallery/',views.admin_gallery),
    path('admin_gallerytb/',views.admin_gallerytb),
    path('admin_galldlt/',views.admin_galldlt),
     path('admin_service_booking/',views.admin_servicebooking),
    path('admin_contacttb/',views.admin_contacttb),
    path('admin_usertb/',views.admin_usertb),
]