# Generated by Django 4.2.17 on 2024-12-09 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelpackages', '0001_travelpackages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='travelpackage',
            options={'verbose_name': 'pacote de viagem', 'verbose_name_plural': 'pacotes de viagens'},
        ),
        migrations.AddField(
            model_name='travelpackage',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]
