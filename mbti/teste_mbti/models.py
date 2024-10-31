from django.db import models
from django.conf import settings
import os, json

data = open(os.path.join(settings.BASE_DIR,"teste_mbti\\json\\simple_mbti_questions.json"), "r", encoding= 'utf-8')
data = json.load(data)