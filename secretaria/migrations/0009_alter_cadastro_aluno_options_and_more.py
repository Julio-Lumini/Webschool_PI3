# Generated by Django 5.0.2 on 2025-03-06 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0008_alter_cadastro_professor_turma'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastro_aluno',
            options={'ordering': ('nome',), 'verbose_name': 'Cadastro de Aluno', 'verbose_name_plural': 'Cadastros de Alunos'},
        ),
        migrations.AlterModelOptions(
            name='cadastro_professor',
            options={'ordering': ('nome',), 'verbose_name': 'Cadastro de Professor', 'verbose_name_plural': 'Cadastros de Professores'},
        ),
        migrations.AlterModelOptions(
            name='historicochamada',
            options={'verbose_name': 'Histórico de Chamada', 'verbose_name_plural': 'Históricos de Chamada'},
        ),
        migrations.AlterModelOptions(
            name='turma',
            options={'verbose_name': 'Turma', 'verbose_name_plural': 'Turmas'},
        ),
        migrations.RemoveField(
            model_name='cadastro_professor',
            name='foto',
        ),
        migrations.AlterField(
            model_name='cadastro_aluno',
            name='cadunico',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastro_aluno',
            name='foto',
            field=models.ImageField(blank=True, default='perfil_aluno/default_aluno.jpg', null=True, upload_to='perfil_aluno'),
        ),
        migrations.AlterField(
            model_name='cadastro_aluno',
            name='periodo',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastro_aluno',
            name='ra',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastro_aluno',
            name='status_presenca',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro_aluno',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='alunos_cadastro', to='secretaria.turma'),
        ),
        migrations.AlterField(
            model_name='cadastro_professor',
            name='telefone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastro_professor',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='professores', to='secretaria.turma'),
        ),
        migrations.AlterField(
            model_name='historicochamada',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='historicochamada',
            name='periodo',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicochamada',
            name='total_alunos_presentes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='historicochamada',
            name='turma',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='secretaria.turma'),
        ),
    ]
