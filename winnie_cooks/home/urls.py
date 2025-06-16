from django.urls import path
from . import views

urlpatterns = [
    path('',views.homep,name='home'),
]