from django.db import models
from django.conf import settings
import os, json

data = open(os.path.join(settings.BASE_DIR,"teste_mbti\\json\\simple_mbti_questions.json"), "r", encoding= 'utf-8')
data = json.load(data)
class respostas(models.Model):

    id = models.AutoField(primary_key=True)
    pergunta_1 = models.TextField(max_length=11)
    pergunta_2 = models.TextField(max_length=11)
    pergunta_3 = models.TextField(max_length=13)
    pergunta_4 = models.TextField(max_length=13)
    perfil_MBTI = models.TextField(max_length=2)

    def __str__(self):
        return "Resposta"