from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostFetch, name='postfetch'),
    path('post/<int:id>/', views.PostFetchById, name='postfetchbyid'),
]