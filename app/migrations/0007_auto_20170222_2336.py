# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_candidato_ensino_superior'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Candidato',
        ),
    ]
