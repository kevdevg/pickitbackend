# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-18 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='descripion',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
