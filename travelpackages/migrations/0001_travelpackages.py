# Generated by Django 5.1.4 on 2024-12-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
 initial = True
 dependencies = []

 operations = [
  migrations.CreateModel(
   name='TravelPackage',
   fields=[
    ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    ('name', models.CharField(max_length=255, verbose_name='Nome')),
    ('original_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço Original')),
    ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço com Desconto')),
    ('image', models.ImageField(upload_to='travelpackages', verbose_name='Imagem')),
    ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
    ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
   ],
   options={
    'db_table': 'travelpackages',
   },
  ),
 ]