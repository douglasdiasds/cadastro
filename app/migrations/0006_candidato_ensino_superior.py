# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_candidato_docfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='Ensino_superior',
            field=models.BooleanField(default=False),
        ),
    ]
