# Generated by Django 3.0.8 on 2020-07-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='valor_total',
            field=models.FloatField(default=1, verbose_name='valor_total'),
            preserve_default=False,
        ),
    ]
