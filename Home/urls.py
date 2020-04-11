from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('information/', views.information),
    path('contact/', views.contact),
]