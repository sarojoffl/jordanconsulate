from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('useful-link/', views.useful_link, name='useful_link'),
    path('articles/', views.articles, name='articles'),
    path('contact/', views.contact, name='contact'),
    path('converters/', views.converters_view, name='converters'),
]
