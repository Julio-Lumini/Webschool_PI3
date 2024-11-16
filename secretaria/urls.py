from django.urls import path
from . import views

urlpatterns = [
    path('home_secretaria/', views.home_secretaria, name='home_secretaria'),
    path('cadastro_professor/', views.cadastro_professor, name='cadastro_professor'),
    path('cadastro_aluno/', views.cadastro_aluno, name='cadastro_aluno'),
    path('relatorios_secretaria/', views.relatorios_secretaria, name='relatorios_secretaria'),
    path('relatorios_diarios/', views.relatorios_diarios, name='relatorios_diarios'),
    path('filtrar_relatorio_diario/', views.filtrar_relatorio_diario, name='filtrar_relatorio_diario'),
    path('listar_professores/', views.listar_professores, name='listar_professores'),
    path('editar_professor/<int:professor_id>/', views.editar_professor, name='editar_professor'),
]