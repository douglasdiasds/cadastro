# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_candidato_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='cover_letter',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='candidato',
            name='linkedin',
            field=models.URLField(max_length=100, default=''),
        ),
    ]
