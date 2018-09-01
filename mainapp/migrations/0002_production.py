# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('p_id', models.IntegerField(serialize=False, primary_key=True)),
                ('p_name', models.CharField(unique=True, max_length=20)),
                ('p_subject', models.CharField(default=b'Headder', max_length=30)),
                ('p_introduce', models.TextField()),
                ('p_images', models.ImageField(upload_to=b'production')),
                ('p_link', models.CharField(default=b'', max_length=b'300')),
            ],
        ),
    ]
