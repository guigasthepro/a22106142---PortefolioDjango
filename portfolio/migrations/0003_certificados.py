# Generated by Django 4.2.2 on 2023-06-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_projetopessoais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('emissao', models.DateTimeField()),
                ('entidade', models.CharField(max_length=20)),
            ],
        ),
    ]
