from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome_to_store, name='welcome'),
]