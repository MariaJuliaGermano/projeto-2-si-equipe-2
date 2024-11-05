from django.shortcuts import render, redirect
from django.conf import settings
import json, os
from .models import respostas

def home(request):
    if request.method == "GET":
        data = open(os.path.join(settings.BASE_DIR,"teste_mbti\\json\\simple_mbti_questions.json"), "r", encoding= 'utf-8')
        data = json.load(data)
        context = {'data':data}
        return render(request, 'teste_mbti/testepersonalidade.html', context=context)
    elif request.method == "POST":
        receivedData = request.POST["data"]
        receivedData = receivedData.split(",")

        pergunta_1 = ""
        pergunta_2 = ""
        pergunta_3 = ""
        pergunta_4 = ""
        tabela = respostas()

        for n in range(0, 11):
            pergunta_1 += receivedData[n]
        for n in range(11, 22):
            pergunta_2 += receivedData[n]
        for n in range(22, 35):
            pergunta_3 += receivedData[n]
        for n in range(35, 48):
            pergunta_4 += receivedData[n]

        tabela.pergunta_1 = pergunta_1[:]
        tabela.pergunta_2 = pergunta_2[:]
        tabela.pergunta_3 = pergunta_3[:]
        tabela.pergunta_4 = pergunta_4[:]

        tabela.save() 

        #print("Incoming info: " + receivedData[:])
        return redirect('results')

def results(request):
    return render(request, 'teste_mbti/resultado.html')