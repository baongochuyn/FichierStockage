# version1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('upload/', views.upload, name='upload'),   
    path('download/<str:encrypted_metadata>/', views.download, name='download'),
]
