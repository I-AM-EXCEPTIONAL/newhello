from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html', {})


def About(request):
    return render(request, "About.html")


def Contact(request):
    return render(request, "Contact.html")
    

def Services(request):
    return render(request,"Services.html")
    