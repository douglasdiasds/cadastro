# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170222_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('e_mail', models.EmailField(default='', max_length=100)),
                ('github', models.URLField(default='')),
                ('linkedin', models.URLField(default='', max_length=100)),
                ('cover_letter', models.TextField(default='')),
                ('Ensino_superior', models.BooleanField(default=False)),
                ('docfile', models.FileField(blank=True, upload_to='/home/douglas/Documentos/Django/my-second-blog/site_/media', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Criterios',
        ),
    ]
