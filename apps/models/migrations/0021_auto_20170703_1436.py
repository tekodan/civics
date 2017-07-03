# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-03 14:36
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0020_city_country_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.AlterField(
            model_name='city',
            name='country_test',
            field=django_countries.fields.CountryField(help_text='¿A qué país pertenece la ciudad?', max_length=2, null=True, verbose_name='País'),
        ),
    ]
