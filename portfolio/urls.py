from django.urls import path
from . import views

app_name = 'portefolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('projetoscurso', views.projetoscurso_page_view, name='projetocurso'),
    path('projetospessoais', views.projetospessoais_page_view, name='projetospessoais'),
    path('projetosescola', views.projetosescola_page_view, name='projetosescola'),
    path('sobre', views.sobre_page_view, name='sobre'),

    path('aptidoes', views.aptidoes_page_view, name='aptidoes'),
    path('blog', views.blog_page_view, name='blog'),
    path('educacao', views.educacao_page_view, name='educacao'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('noticias', views.noticias_page_view, name='noticias'),
    path('tecnicas', views.tecnicas_page_view, name='tecnicas'),
    path('tecnologiasexistentes', views.tecnologiasexistentes_page_view, name='tecnologiasexistentes'),
    path('laboratorios', views.laboratorios_page_view, name='laboratorios')
]