from django import forms
from .models import cadastro

class formCadastro(forms.ModelForm):

    nome_completo = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs= {'placeholder': 'Digite o seu nome completo'}))
    turma = forms.CharField(max_length=1, required=True, widget=forms.TextInput(attrs= {'placeholder': 'Digite a sua turma'}))
    email = forms.EmailField(max_length=40, required=True, widget=forms.EmailInput(attrs= {'placeholder': 'Digite o seu email institucional'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'Digite uma senha forte'}), required=True)

    class Meta:
        model = cadastro
        fields = '__all__'

class formLogin(forms.ModelForm):

    email = forms.EmailField(max_length=40, required=True, widget=forms.EmailInput(attrs= {'placeholder': 'Digite o seu email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'Digite o sua senha'}), required=True)

    class Meta:
        model = cadastro
        fields = '__all__'
