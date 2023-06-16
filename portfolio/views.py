from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *
from .models import *
# Create your views here.
from django.shortcuts import render

def logout_view(request):
    logout(request)
    return render(request, 'login.html',{'message': "Logged Out"})

def login_view (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None :
            login(request, user)
            context = {'publicacaos': Publicacao.objects.all()}
            return render(request, 'blog.html', context)
        else :
            return render(request, 'login.html', {
                'menssage': "Invalid credentials"
            })
    return render (request,'login.html' )

def aptidoes_page_view(request):
    context = {'educacaos': Educacao.objects.all(),
               'competencias': Competencia.objects.all(),
               'certificados': Certificados.objects.all(),
               'linguas': Lingua.objects.all(),
               'interesses': Interesse.objects.all(),
               }
    return render(request, 'aptidoes.html', context)


def blog_page_view(request):
    context = {'posts': Publicacao.objects.all()}
    return render(request, 'blog.html', context)
def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'licenciatura.html', context)

def laboratorios_page_view(request):
    context = {'laboratorios': Laboratorio.objects.all()}
    return render(request, 'laboratorios.html', context)

def bandas_page_view(request):
    context = {'bandas': Banda.objects.all()}
    return render(request, 'banda.html', context)
def noticias_page_view(request):
    context = {'noticias': Noticia.objects.all()}
    return render(request, 'noticias.html',context)

def tecnologiasexistentes_page_view(request):
    context = {'tecnologiasexistentes': Tecnologiawebsite.objects.all()}
    return render(request, 'tecnologiasexistentes.html',context)

def tecnicas_page_view(request):
    return render(request, 'tecnicas.html')

def home_page_view(request):
    return render(request, 'home.html')

def contacto_page_view(request):
    return render(request, 'contacto.html')

def projetoscurso_page_view(request):
    context = {'tfcs': TFC.objects.all()}
    return render(request, 'projetoscurso.html',context)

def projetospessoais_page_view(request):
    context = {'projetospessoais': ProjetoPessoais.objects.all()}
    return render(request, 'projetospessoais.html',context)



def projetosescola_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'projetosescola.html',context)

def sobre_page_view(request):
    context = {'tecnologiasusadas' : TecnologiaUsadas.objects.all()}
    return render(request, 'sobre.html',context)

@login_required
def apagarPost_page_view(request, blog_id):
    Publicacao.objects.get(id=blog_id).delete()
    return HttpResponseRedirect(reverse('portefolio:blog'))

@login_required
def editarPost_page_view(request, blog_id):

    blog = Publicacao.objects.get(id=blog_id)
    form = PublicacaoForm(request.POST or None, instance=blog)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portefolio:blog'))

    context = {'form': form, 'blog_id': blog_id,}

    return render(request, 'editarpost.html')