from django.urls import path
from . import views

app_name = 'galeria'

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/', views.imagem, name='imagem'),
]