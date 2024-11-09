from django.shortcuts import render, redirect, get_object_or_404
from .form import formCadastro, formLogin
from .models import cadastro as table
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.hashers import make_password

def cadastro(request):

    form = formCadastro(request.POST)

    if not form.is_valid():
        context = {'formulario':form}
        return render(request, 'auth_mbti/cadastro.html', context)

    perfil = form.save(commit=False)
    perfil.senha = make_password(perfil.senha)
    perfil.save()

    tabela = cadastro()
    tabela.nome_completo = perfil.nome_completo
    tabela.turma = perfil.turma
    tabela.email = perfil.email
    tabela.senha = perfil.senha
    tabela.save()
    
    return redirect('login')

def verificarLogin(request):
    formulario = formLogin(request.POST)
    tabela = table()

    user = authenticate(username=perfil.email, password=perfil.senha)
    if user:
        # A função django-login é necessária para que o usuário seja considerado logado no sistema.
        # A biblioteca Django mantém o estado do usuário logado usando um cookie.
        # A função django-login cria e atualiza esse cookie para que o usuário seja considerado logado.
        django_login(request, user)
        return render(request, 'teste_mbti/testedepersonalidade.html')

    else:
        if not formulario.is_valid():
            context = {'formulario':formulario}
            return render(request, 'auth_mbti/cadastro.html', context)
    
        perfil = formulario.save(commit=False)
        senhas = tabela.objects.values_list('senha', flat=True)

        if perfil.senha in senhas:
            context = {'dadosUsuario':tabela.objects.filter(senha=perfil.senha)}

            return render(request, 'teste_mbti/testedepersonalidade.html')
        
#===================== Views =====================

def cadastrar(request):

    if request.method == 'POST':
        return cadastro(request)
    
    elif request.method == 'GET':
        context = {'formulrio':formCadastro()}
        return render(request, 'auth_mbti/cadastro.html', context=context)


def login(request):

    if request.method == 'GET':
      context = {'formulario': formLogin}
      return render(request, 'auth_mbti/login.html', context)
  
    elif request.method == 'POST':
        return verificarLogin(request)

def logout(request):
      return render(request, 'auth_mbti/logout.html')