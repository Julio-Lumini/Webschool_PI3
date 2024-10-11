from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('chamada/', views.chamada, name='chamada'),
    path('atualizar-presenca/', views.atualizar_presenca, name='atualizar_presenca'),
    path('gerar-relatorio/', views.gerar_relatorio, name='gerar_relatorio'),
        
]
