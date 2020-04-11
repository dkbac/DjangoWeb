from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('information/', views.information, name='information'),
    path('contact/', views.contact, name='contact'),
]

