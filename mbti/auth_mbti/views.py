from django.shortcuts import render, redirect, HttpResponse
from .form import formCadastro, formLogin
from .models import cadastro as table
from teste_mbti.models import respostas
from hashlib import sha256, sha512
from auth_mbti.models import arquivosExel
import pandas

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

            email_confirm = request.POST['email_confirm']

            if email_confirm == form['email'].value():
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
                'email_divergente':'Os emails devem se iguais nos dois campos',
                'formulario':formCadastro()
                }
                return render(request, 'auth_mbti/cadastro.html', context)
        
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
        response = redirect('home')
        response.set_cookie('logged', True, max_age=1500, secure=True, httponly=True)

        email_logged = sha256(user.email.encode()).hexdigest()
        email_logged = sha512(email_logged.encode()).hexdigest()
        
        response.set_cookie('logged_info', email_logged, max_age=1500, secure=True, httponly=True)

        try:
            user_test = respostas.objects.get(chave = user.id)
            response.set_cookie('test_info', 'True', max_age=1500, secure=True, httponly=True)

        except:
            response.set_cookie('test_info', 'False', max_age=1500, secure=True, httponly=True)

        return response 

    else:
        context = {
            'erro_login':'Email ou senha incorretos',
            'formulario': formLogin
            }
        return render(request, 'auth_mbti/login.html', context)
    
def importExel(request):

    pathArquivo = request.POST.get('resposta')

    database = pandas.read_excel(pathArquivo)

    for idx, linha  in database.iterrows():
        email = linha['email institucional']

        try:
            user = table.objects.get(email=email)
        
        except:

            perfil = table()
            perfil.nome_completo = linha['nome completo'] 
            perfil.turma = linha['turma']
            perfil.email = email

            senha = '0000'
            senha_hash = sha256(senha.encode()).hexdigest()
            perfil.senha = senha_hash

            perfil.curso = linha['curso']
            perfil.save()
            
    return HttpResponse('cadastro realizado com sucesso!')

# def verificarConfirmacao(request):
#     senha = request.POST.get('senha')

#     if senha == 'senha de confirmação':
#         return render(request, 'auth_mbti/cadExel.html')
    
#     else:
#         return render(request, 'auth_mbti/confirmacao.html')
    
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
      response.delete_cookie('logged_info')

      return response
  
    elif request.method == 'POST':
        return verificarLogin(request)

def logout(request):
      return render(request, 'auth_mbti/logout.html')

def cadExel(request):

    if request.method == 'GET':
        arquivos =  arquivosExel.objects.values_list('arquivo', flat=True)
        context = {'arquivos': arquivos}

        return render(request, 'auth_mbti/cadExel.html', context)

    elif request.method == 'POST':
        return importExel(request)
        
# def confirmacao(request):

#     if request.method == 'GET':
#         return render(request, 'auth_mbti/confirmacao.html')
    
#     elif request.method == 'POST':
#         senha = request.POST.get('senha')

#         if senha == 'senha de confirmação':
#             return render(request, 'auth_mbti/cadExel.html')
        
#         else:
#             return render(request, 'auth_mbti/confirmacao.html')
    
