from django.urls import path
from . import views

urlpatterns =[
	path('', views.home_view, name= 'home-view'),
	path('contact', views.contact_view, name= 'contact-view'),
	path('about', views.about_view, name= 'about-view'),
	path('services', views.services_view, name= 'services-view'),
	path('appointment', views.appointment_view, name= 'appointment-view'),
]