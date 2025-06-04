from django.shortcuts import render,HttpResponse

def welcome_to_store(request):
    return HttpResponse("<h2>welcome to my store</h2>")
# Create your views here.
