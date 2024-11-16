from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('sair/', views.sair, name='sair'),
]
