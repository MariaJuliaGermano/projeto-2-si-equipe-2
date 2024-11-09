from django import forms
from .models import cadastro

class formCadastro(forms.ModelForm):

    nome_completo = forms.CharField(max_length=100, required=True, widget=forms.TextInput)
    turma = forms.CharField(max_length=1, required=True, widget=forms.TextInput)
    email = forms.EmailField(max_length=40, required=True, widget=forms.EmailInput)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = cadastro
        fields = '__all__'

class formLogin(forms.ModelForm):

    email = forms.EmailField(max_length=40, required=True, widget=forms.EmailInput)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = cadastro
        fields = '__all__'
