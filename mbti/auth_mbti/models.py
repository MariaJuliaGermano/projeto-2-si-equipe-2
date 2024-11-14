from django.db import models
from django.contrib.auth.models import User
import random

def generate_unique_ra():
    while True:
        ra = str(random.randint(10**9, 10**10 - 1))  # Gera um RA de 10 dígitos
        if not Aluno.objects.filter(ra=ra).exists() and not Professor.objects.filter(ra=ra).exists():
            return ra

class cadastro(models.Model):

    id = models.AutoField(primary_key=True)
    nome_completo = models.TextField(max_length=200, blank=False, null=False)
    turma = models.TextField(max_length=1, blank=False, null=False)
    curso = models.TextField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=40, blank=False, null=False)
    senha = models.TextField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.nome_completo

class Turma(models.Model):
    nome = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.nome

class Professor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor', null=True)
    email= models.EmailField(null=True, max_length=254)
    ra = models.CharField(max_length=10, unique=True, default=generate_unique_ra)  # Função explícita para RA

class Aluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="aluno", null=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="alunos", null=True)
    email = models.EmailField(null=True, max_length=254)  # Garantir emails únicos
    ra = models.CharField(max_length=10, unique=True, default=generate_unique_ra)
