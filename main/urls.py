from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('visa-info/', views.visa_info, name='visa_info'),
    path('apply-form/', views.apply_form, name='apply_form'),
    path('useful-link/', views.useful_link, name='useful_link'),
    path('articles/', views.articles, name='articles'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]
