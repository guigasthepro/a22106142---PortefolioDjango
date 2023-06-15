# Generated by Django 4.2.2 on 2023-06-14 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=2)),
                ('ects', models.IntegerField()),
                ('ano_letivo', models.CharField(max_length=20)),
                ('topicos_abordados', models.TextField()),
                ('ranking', models.IntegerField()),
                ('link_cadeira', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Educacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacao', models.CharField(max_length=40)),
                ('curso', models.CharField(max_length=40)),
                ('local', models.CharField(max_length=20)),
                ('periodo', models.CharField(max_length=30)),
                ('logotipo', models.ImageField(upload_to='static/portfolio/images')),
            ],
        ),
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('descricao', models.TextField(max_length=1000)),
                ('imagem', models.ImageField(upload_to='static/portfolio/images')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('descricao', models.TextField(max_length=1000)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lingua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('nivel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('descricao', models.TextField(max_length=1000)),
                ('imagem', models.ImageField(upload_to='static/portfolio/images')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('link_lusofona', models.CharField(blank=True, max_length=1000, null=True)),
                ('link_linkedin', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, upload_to='static/portfolio/images')),
                ('autor', models.CharField(max_length=25)),
                ('data', models.DateTimeField()),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=2000)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('acronimo', models.CharField(blank=True, max_length=10)),
                ('anoCriacao', models.IntegerField()),
                ('criador', models.CharField(max_length=80)),
                ('logotipo', models.ImageField(upload_to='static/portfolio/images')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('descricao', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologiawebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('acronimo', models.CharField(blank=True, max_length=10)),
                ('anoCriacao', models.IntegerField()),
                ('criador', models.CharField(max_length=80)),
                ('logotipo', models.ImageField(upload_to='static/portfolio/images')),
                ('codigo', models.ImageField(upload_to='static/portfolio/images')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('descricao', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TFC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('imagem', models.ImageField(blank=True, upload_to='static/portfolio/images')),
                ('anoRealizacao', models.IntegerField()),
                ('sumario', models.CharField(max_length=500)),
                ('link_relatorio', models.CharField(max_length=1000)),
                ('linkGitHub', models.CharField(blank=True, max_length=1000, null=True)),
                ('linkYt', models.CharField(blank=True, max_length=1000, null=True)),
                ('autor', models.ManyToManyField(related_name='autor', to='portfolio.pessoa')),
                ('orientador', models.ManyToManyField(related_name='orientador', to='portfolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=500)),
                ('imagem', models.ImageField(blank=True, upload_to='static/portfolio/images')),
                ('anoRealizacao', models.IntegerField()),
                ('linkGitHub', models.CharField(blank=True, max_length=1000, null=True)),
                ('linkYt', models.CharField(blank=True, max_length=1000, null=True)),
                ('participantes', models.ManyToManyField(blank=True, to='portfolio.pessoa')),
                ('tecnologias', models.ManyToManyField(blank=True, to='portfolio.tecnologia')),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descricao', models.TextField(max_length=1000)),
                ('cadeira', models.ManyToManyField(blank=True, to='portfolio.cadeira')),
                ('projetos', models.ManyToManyField(blank=True, to='portfolio.projeto')),
            ],
        ),
        migrations.AddField(
            model_name='cadeira',
            name='docente_teorica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='docentes_praticas',
            field=models.ManyToManyField(related_name='professor_pratica', to='portfolio.pessoa'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='linguagens',
            field=models.ManyToManyField(blank=True, to='portfolio.tecnologia'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='projetos',
            field=models.ManyToManyField(blank=True, to='portfolio.projeto'),
        ),
    ]
