# Generated by Django 5.0.4 on 2024-11-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0005_historicochamada_cadastro_professor_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro_aluno',
            name='cidade',
            field=models.CharField(default=8, max_length=50),
            preserve_default=False,
        ),
    ]
