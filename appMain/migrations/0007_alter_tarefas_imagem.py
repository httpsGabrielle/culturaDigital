# Generated by Django 4.1.1 on 2022-11-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMain', '0006_tarefas_imagem_alter_tarefas_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
