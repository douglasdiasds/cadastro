# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Candidate'),
        ),
    ]