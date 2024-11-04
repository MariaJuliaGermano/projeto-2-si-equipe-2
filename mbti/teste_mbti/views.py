from django.shortcuts import render, redirect
from django.conf import settings
import json, os

def home(request):
    if request.method == "GET":
        data = open(os.path.join(settings.BASE_DIR,"teste_mbti\\json\\simple_mbti_questions.json"), "r", encoding= 'utf-8')
        data = json.load(data)
        context = {'data':data}
        return render(request, 'teste_mbti/testepersonalidade.html', context=context)
    elif request.method == "POST":
        receivedData = request.POST["data"]
        receivedData = receivedData.split(",")
        print("Incoming info: " + receivedData[1])
        return redirect('results')

def results(request):
    return render(request, 'teste_mbti/resultado.html')