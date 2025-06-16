from django.shortcuts import render

# Create your views here.
def available_dishes(requests):
    return render(requests,'menu/dishes.html')
