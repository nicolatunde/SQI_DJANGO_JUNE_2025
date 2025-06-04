from django.urls import path

from . import views

urlpatterns = [
    path('greetme/',views.greetme,name='greetme')
]