# Generated by Django 4.1.1 on 2022-12-16 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMain', '0012_tarefas_criado_em'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefas',
            name='criado_em',
        ),
    ]
