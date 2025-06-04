from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests,'profile_app/index.html')

def goals(requests):
    return render(requests,'profile_app/goals.html')

def hobbies(requests):
    return render(requests,'profile_app/hobbies.html')
