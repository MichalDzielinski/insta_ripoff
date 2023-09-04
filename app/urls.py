from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='view'),
    path('add/', views.add, name='add'),
]