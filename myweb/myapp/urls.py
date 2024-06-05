from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
     path('home/', views.portfolio, name='portfolio'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('ict_training_request/', views.ict_training_request, name='ict_training_request'),
    path('success/', views.success, name='success'),  # Define a success page




]


