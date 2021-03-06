# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 08:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170329_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='appraiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Candidate', unique=True),
        ),
    ]
