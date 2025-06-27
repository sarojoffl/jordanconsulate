from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def useful_link(request):
    return render(request, 'main/useful_link.html')

def articles(request):
    return render(request, 'main/articles.html')

def contact(request):
    return render(request, 'main/contact.html')