from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def visa_info(request):
    return render(request, 'main/visa_info.html')

def apply_form(request):
    return render(request, 'main/apply_form.html')

def useful_link(request):
    return render(request, 'main/useful_link.html')

def articles(request):
    return render(request, 'main/articles.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def contact(request):
    return render(request, 'main/contact.html')