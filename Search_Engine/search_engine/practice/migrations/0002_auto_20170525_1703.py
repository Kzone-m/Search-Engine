# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(choices=[('A', 'a'), ('B', 'b'), ('C', 'c')], max_length=32, verbose_name='球団名'),
        ),
    ]