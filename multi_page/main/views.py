from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests,'main/home.html')


def about(requests):
    return render(requests,'main/about.html')


def contact(requests):
    return render(requests,'main/contact.html')


