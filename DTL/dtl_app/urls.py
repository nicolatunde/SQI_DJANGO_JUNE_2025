from django.urls import path
from . import views

urlpatterns =[
    path('dtl/',views.dtl,name='dtl'),
]