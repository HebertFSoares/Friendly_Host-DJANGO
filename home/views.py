from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Perfil
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import AdicionarVagaForm
from .models import VagaCasa


def is_estudante(user):
    try:
        perfil = Perfil.objects.get(usuario=user)
        return perfil.user_type == 'estudante'
    except Perfil.DoesNotExist:
        return False

def is_anfitriao(user):
    try:
        perfil = Perfil.objects.get(usuario=user)
        return perfil.user_type == 'anfitriao'
    except Perfil.DoesNotExist:
        return False

@login_required
def home_estudante(request):
    if not is_estudante(request.user) and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('error'))
    return render(request, 'home_estudante.html')

@login_required
def home_anfitriao(request):
    if not is_estudante(request.user) and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('error'))
    return render(request, 'home_anfitriao.html')

def error(request):
    return render(request, 'erro.html')

from django.shortcuts import render, redirect
from .forms import AdicionarVagaForm
from .models import VagaCasa

def adicionar_vaga(request):
    if request.method == 'POST':
        form = AdicionarVagaForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário e criar uma nova vaga de casa
            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            localizacao = form.cleaned_data['localizacao']
            capacidade = form.cleaned_data['capacidade']
            regras_casa = form.cleaned_data['regras_casa']
            informacoes_familia = form.cleaned_data['informacoes_familia']
            contato = form.cleaned_data['contato']
            
            vaga = VagaCasa(
                titulo=titulo,
                descricao=descricao,
                localizacao=localizacao,
                capacidade=capacidade,
                regras_casa=regras_casa,
                informacoes_familia=informacoes_familia,
                contato=contato
            )
            vaga.save()
            
            # Redirecionar para a página de sucesso ou exibir uma mensagem de confirmação
            return ("Certo")  # substitua 'pagina_sucesso' pela URL correta da página de sucesso
        
    else:
        form = AdicionarVagaForm()
    
    return render(request, 'adicionar_vaga.html', {'form': form})
