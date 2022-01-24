from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>', views.viewPhoto, name='photo'),
    path('add/', views.AddPhoto, name='add'),
]