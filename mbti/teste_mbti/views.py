from django.shortcuts import render, redirect
from django.conf import settings
import json, os
from .models import respostas
from math import ceil

def index(request):
    return redirect('cadastro')

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
        perfil_mbti = ""
        tabela = respostas()

        for n in range(0, 11):
            pergunta_1 += receivedData[n]
        for n in range(11, 22):
            pergunta_2 += receivedData[n]
        for n in range(22, 35):
            pergunta_3 += receivedData[n]
        for n in range(35, 48):
            pergunta_4 += receivedData[n]

        resposta_S = receivedData.count("S")
        resposta_N = receivedData.count("N")
        resposta_F = receivedData.count("F")
        resposta_T = receivedData.count("T")
        resposta_J = receivedData.count("J")
        resposta_P = receivedData.count("P")

        if resposta_S > resposta_N:
            perfil_mbti += "S"
            if resposta_P > resposta_J:
                perfil_mbti += "P"
            else:
                perfil_mbti += "J"

        elif resposta_N > resposta_S:
            perfil_mbti += "N"
            if resposta_F > resposta_T:
                perfil_mbti += "F"
            else:
                perfil_mbti += "T"

        tabela.pergunta_1 = pergunta_1[:]
        tabela.pergunta_2 = pergunta_2[:]
        tabela.pergunta_3 = pergunta_3[:]
        tabela.pergunta_4 = pergunta_4[:]
        tabela.perfil_MBTI = perfil_mbti[:]

        tabela.save() 

        return redirect('results')

def results(request):

    tabela = respostas.objects.latest('id')
    perfil = tabela.perfil_MBTI

    if perfil == "SJ":
        context = {
            'perfil':"GUARDIÃO", 
            'sigla': "SJ",
            'descrição': "Concreto e cooperativo, procura segurança, está preocupados com a responsabilidade e dever. Sua maior força é a logística. Seu ponto forte é organização. É excelentes em facilitar (para os demais), verificar (serviço dos demais) e dar apoio em geral."
            }
    elif perfil == "SP":
        context = {
            'perfil':"ARTESÃO", 
            'sigla': "SP",
            'descrição': "Concreto e pragmático, procura estimulação e preocupa-se em causar impacto. Sua maior força é a tática. É excelentes na resolução de problemas, agilidade, manipulação de ferramentas, instrumentos e equipamentos."
            }
    elif perfil == "NF":
        context = {
            'perfil':"IDEALISTA", 
            'sigla': "NF",
            'descrição': "Abstrato e cooperativo, procura significado e importância, se preocupa com crescimento pessoal e encontrar sua própria identidade. Sua maior força é a diplomacia. Destaca-se por deixar situações mais claras e inspirar pessoas."
            }
    elif perfil == "NT":
        context = context = {
            'perfil':"RACIONAL", 
            'sigla': "NT",
            'descrição': "Abstrato e pragmático, procura maestria e autocontrole. Se preocupa com o próprio conhecimento e competência. Sua maior força é a estratégia. Destacam-se em investigações lógicas como engenharia, conceitos, teorias e coordenação."
            }
        
    pergunta_1 = list(tabela.pergunta_1)
    len_E = pergunta_1.count("E")
    extrovertido = (len_E / 11) * 100

    pergunta_2 = list(tabela.pergunta_2)
    len_N = pergunta_2.count("N")
    intuitivo = (len_N / 11) * 100
    print(intuitivo)

    pergunta_3 = list(tabela.pergunta_3)
    len_T = pergunta_3.count("T")
    analitico = (len_T / 13) * 100

    pergunta_4 = list(tabela.pergunta_4)
    len_J = pergunta_4.count("E")
    planejador = (len_J / 13) * 100

    len_P = pergunta_4.count("P")
    assertivo = (len_P / 13) * 100

    context['extrovertido'] = ceil(extrovertido)
    context['intuitivo'] = ceil(intuitivo)
    context['analitico'] = ceil(analitico)
    context['planejador'] = ceil(planejador)
    context['assertivo'] = ceil(assertivo)

    return render(request, 'teste_mbti/resultado.html', context)