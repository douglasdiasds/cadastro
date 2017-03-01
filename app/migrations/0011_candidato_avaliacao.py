# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170223_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='avaliacao',
            field=models.ForeignKey(to='app.Criterio', default=''),
        ),
    ]
