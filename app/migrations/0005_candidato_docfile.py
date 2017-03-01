# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170222_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='docfile',
            field=models.FileField(upload_to='/home/douglas/Documentos/Django/my-second-blog/site_/media', null=True, blank=True),
        ),
    ]
