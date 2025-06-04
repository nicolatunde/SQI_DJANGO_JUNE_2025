from django.urls import path
from . import views

urlpatterns = [
    path("", views.bool_list,name='books'),
    path("special/", views.special_book,name='special_books'),
]
