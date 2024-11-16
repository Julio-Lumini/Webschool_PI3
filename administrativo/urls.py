from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrativo_home, name='administrativo_home'),
    path('cadastro_materiais/', views.cadastro_materiais, name='cadastro_materiais'),
    path('controle_merenda/', views.controle_merenda, name='controle_merenda'),
    path('importar_merenda/', views.importar_merenda, name='importar_merenda'),
    path('exportar_merenda/', views.exportar_merenda, name='exportar_merenda'),
    path('analise_merenda/', views.analise_merenda, name='analise_merenda'),
]
