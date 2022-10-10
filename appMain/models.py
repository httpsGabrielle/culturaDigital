from django.db import models

class Materia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Categoria(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tipo

class Tarefas(models.Model):
    nome = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    publicado = models.BooleanField(default=False)

    class Meta:
        verbose_name= 'Tarefa'

    def __str__(self):
        return self.nome
