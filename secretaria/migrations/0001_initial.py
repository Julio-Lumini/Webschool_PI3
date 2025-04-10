# Generated by Django 5.0.4 on 2024-05-11 02:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro_Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.ImageField(upload_to='perfil_professor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='secretaria.turmas')),
            ],
        ),
    ]
