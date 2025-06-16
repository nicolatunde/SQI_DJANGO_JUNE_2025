from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from library.models import Book
from .models import Author


def all_authors(request):
    return render(request,"authors/List_of_Authors.html")

def book_signings(request):
    return render(request,"authors/booksignings.html")


def mvt(request):
    all_authors = Author.objects.all()
    all_books = Book.objects.all()
    context = {
        "authors": all_authors,
        "books": all_books,
    }
    return render(request,"authors/mvt.html", context)
   

