from django.db import models
from uuid import uuid4

# Create your models here.


class Alunos(models.Model):
    id_aluno = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    rgm = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    turma = models.CharField(max_length=255)
    matricula = models.DateField(auto_now_add=True)