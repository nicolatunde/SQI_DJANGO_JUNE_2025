from django.shortcuts import render

# Create your views here.
def homep(requests):
    return render(requests,'home/home.html')
