from django.db import models
from auth_mbti.models import cadastro 

class respostas(models.Model):

    chave = models.ForeignKey(cadastro, on_delete=models.CASCADE)
    pergunta_1 = models.TextField(max_length=11)
    pergunta_2 = models.TextField(max_length=11)
    pergunta_3 = models.TextField(max_length=13)
    pergunta_4 = models.TextField(max_length=13)
    perfil_MBTI = models.TextField(max_length=2)

    def __str__(self):
        return self.chave.nome_completo

class feedbackmbti(models.Model):

    chave = models.ForeignKey(cadastro, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.chave.nome_completo
