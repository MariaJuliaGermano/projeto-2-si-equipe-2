from django.shortcuts import render

def home(request):
    return render(request, 'teste_mbti/testepersonalidade.html')
