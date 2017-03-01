# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_criterios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Criterios',
            new_name='Criterio',
        ),
    ]
