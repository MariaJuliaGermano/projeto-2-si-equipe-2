from django.shortcuts import render

def home(request):
    return render(request, 'teste_mbti/home.html')
