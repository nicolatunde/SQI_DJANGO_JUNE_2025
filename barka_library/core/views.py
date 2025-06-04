from django.shortcuts import render,HttpResponse

def home(requests):
    return HttpResponse("<h1>welcome to Barka street Library</h1>")


# Create your views here.
