from django.urls import path
from . import views

app_name = 'artist'

urlpatterns = [
    path('artist/', views.artistlistening,name='artist'),
]