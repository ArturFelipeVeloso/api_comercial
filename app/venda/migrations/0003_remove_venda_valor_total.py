# Generated by Django 3.0.8 on 2020-07-04 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0002_venda_valor_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='valor_total',
        ),
    ]