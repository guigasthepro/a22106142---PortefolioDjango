from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Publicacao)
admin.site.register(Cadeira)
admin.site.register(Educacao)
admin.site.register(Pessoa)
admin.site.register(Competencia)
admin.site.register(Interesse)
admin.site.register(Lingua)
admin.site.register(Certificados)
admin.site.register(TecnologiaUsadas)
admin.site.register(Banda)
#Projetos
admin.site.register(Projeto)
admin.site.register(TFC)
admin.site.register(ProjetoPessoais)

#Programação Web
admin.site.register(Tecnologia)
admin.site.register(Laboratorio)
admin.site.register(Noticia)

admin.site.register(Tecnologiawebsite)