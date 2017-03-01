# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_candidato_e_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='github',
            field=models.URLField(default=''),
        ),
    ]
