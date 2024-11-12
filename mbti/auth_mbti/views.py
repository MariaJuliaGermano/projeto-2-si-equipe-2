from django.shortcuts import render, redirect, HttpResponse
from .form import formCadastro, formLogin
from .models import cadastro as table
from django.contrib.auth import login as django_login
from hashlib import sha256

def cadastro(request):

    form = formCadastro(request.POST)

    if not form.is_valid():
        context = {'formulario':form}
        return render(request, 'auth_mbti/cadastro.html', context)

    tabela = table()
    email = form['email'].value()

    try:
        user = table.objects.get(email=email)
        context = {
            'email_existente':'Este email ja está sendo utilizado em uma conta',
            'formulario':formCadastro()
            }
        return render(request, 'auth_mbti/cadastro.html', context)
    
    except:

        senha_confim = request.POST['senha_confirm']

        if senha_confim == form['senha'].value():
            perfil = form.save(commit=False)
            tabela.nome_completo = perfil.nome_completo 
            tabela.turma = perfil.turma
            tabela.email = perfil.email

            senha = perfil.senha
            senha_hash = sha256(senha.encode()).hexdigest()
            tabela.senha = senha_hash

            tabela.curso = perfil.curso
            tabela.save()
            
            return redirect('login')
        
        else:
            context = {
            'senha_divergente':'As senhas devem se iguais nos dois campos',
            'formulario':formCadastro()
            }
            return render(request, 'auth_mbti/cadastro.html', context)

def verificarLogin(request):
    formulario = formLogin(request.POST)
    email = formulario['email'].value()

    senha = formulario['senha'].value()
    senha_hash = sha256(senha.encode()).hexdigest()

    try:
        user = table.objects.get(email=email)
        
    except:
        context = {
            'erro_login':'Email ou senha incorretos',
            'formulario': formLogin()
            }
        return render(request, 'auth_mbti/login.html', context)
    
    if user.senha == senha_hash:
        logado = HttpResponse('logged')
        response = redirect('home')
        response.set_cookie('logged', True, max_age=1500, secure=True, httponly=True)

        return response

    else:
        context = {
            'erro_login':'Email ou senha incorretos',
            'formulario': formLogin
            }
        return render(request, 'auth_mbti/login.html', context)

    #user = authenticate(username=formulario.email, password=formulario.senha)
    # if user:
        # A função django-login é necessária para que o usuário seja considerado logado no sistema.
        # A biblioteca Django mantém o estado do usuário logado usando um cookie.
        # A função django-login cria e atualiza esse cookie para que o usuário seja considerado logado.
        # django_login(request, user)
        # return render(request, 'teste_mbti/testedepersonalidade.html')
#===================== Views =====================

def cadastrar(request):

    if request.method == 'POST':
        return cadastro(request)
    
    elif request.method == 'GET':
        context = {'formulario':formCadastro()}
        return render(request, 'auth_mbti/cadastro.html', context=context)


def login(request):

    if request.method == 'GET':
      context = {'formulario': formLogin()}
      response = render(request, 'auth_mbti/login.html', context)
      response.delete_cookie('logged')
      
      return response
  
    elif request.method == 'POST':
        return verificarLogin(request)

def logout(request):
      return render(request, 'auth_mbti/logout.html')