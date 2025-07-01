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
    path('news/', views.news_view, name='news'),
    path('photo-album/', views.photo_album_view, name='photo_album'),
]
