from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('sair/', views.sair, name='sair'),
    path('cadastro/', views.cadastro, name='cadastro')
]