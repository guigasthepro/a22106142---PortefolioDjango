# Generated by Django 4.2.2 on 2023-06-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_tecnologiausadas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=75)),
                ('estilo', models.CharField(max_length=100)),
            ],
        ),
    ]
