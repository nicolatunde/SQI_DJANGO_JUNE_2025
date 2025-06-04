from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def all_authors(request):
    return render(request,"authors/List_of_Authors.html")

def book_signings(request):
    return render(request,"authors/booksignings.html")