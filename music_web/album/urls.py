from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('', views.home,name='home'),
    path('album/', views.albumlistening,name='album'),
]