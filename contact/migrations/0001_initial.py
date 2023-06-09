# Generated by Django 4.2 on 2023-04-30 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primeiro Nome')),
                ('last_name', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('phone', models.CharField(max_length=50, unique=True, verbose_name='Nº Telefone')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='data de entrada')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('show', models.BooleanField(default=True, verbose_name='Mostrar')),
                ('picture', models.ImageField(blank=True, upload_to='pictures/%Y/%m/', verbose_name='Foto')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.category')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
