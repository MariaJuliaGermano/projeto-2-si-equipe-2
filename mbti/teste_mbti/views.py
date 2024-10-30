from django.shortcuts import render
from django.conf import settings
import json
import os

def home(request):
    if request.method == "GET":
        data = open(os.path.join(settings.BASE_DIR,"teste_mbti\\json\\simple_mbti_questions.json"), "r", encoding= 'utf-8')
        data = json.load(data)
        print(data)
        context = {'data':data}
        return render(request, 'teste_mbti/testepersonalidade.html', context=context)
    elif request.method == "POST":
        return 0