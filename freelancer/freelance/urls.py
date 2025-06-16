from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog,name='blog'),
    path('case_study/', views.case_study,name='case_study'),
    path('pricing/', views.pricing,name='pricing'),
    path('service/', views.service,name='service'),
    path('testimonials/', views.testimonials,name='testimonials'),
]
