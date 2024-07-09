from django.urls import path

from Portfolioapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('contact_form/', views.contact_form, name='Contact_form'),
    path('Contact_form_email/', views.contact_form_email, name='contact_form_email'),
    path('contact_form_success/', views.contact_form_success, name='contact_form_success')
]
