from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostFetch),
    path('post/<int:id>/', views.PostFetchById),
]