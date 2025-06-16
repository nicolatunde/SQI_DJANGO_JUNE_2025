from django.urls import path
from . import views

urlpatterns = [
    path('dishes/',views.available_dishes,name='dishes')
]