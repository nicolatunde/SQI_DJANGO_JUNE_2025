from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests,'bakery/home.html')

def menu(requests):
    return render(requests,'bakery/menu.html')

def about(requests):
    return render(requests,'bakery/about.html')

def contact(requests):
    return render(requests,'bakery/contact.html')


