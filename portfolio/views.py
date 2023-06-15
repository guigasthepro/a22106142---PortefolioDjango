from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
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
	context = {'cadeiras': Cadeira.objects.all()}
	return render(request, 'aptidoes.html', context)
def blog_page_view(request):
	return render(request, 'blog.html')
def educacao_page_view(request):
	return render(request, 'educacao.html')
def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'licenciatura.html', context)

def laboratorios_page_view(request):
	return render(request, 'laboratorios.html')

def noticias_page_view(request):
	return render(request, 'noticias.html')

def tecnologiasexistentes_page_view(request):
	return render(request, 'tecnologiasexistentes.html')

def tecnicas_page_view(request):
	return render(request, 'tecnicas.html')

def home_page_view(request):
	return render(request, 'home.html')

def contacto_page_view(request):
	return render(request, 'contacto.html')

def projetoscurso_page_view(request):
	return render(request, 'projetoscurso.html')

def projetospessoais_page_view(request):
	return render(request, 'projetospessoais.html')

def projetosescola_page_view(request):
	return render(request, 'projetosescola.html')

def sobre_page_view(request):
	return render(request, 'sobre.html')