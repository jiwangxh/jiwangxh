# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('fl_id', models.IntegerField(serialize=False, primary_key=True)),
                ('tl_name', models.CharField(unique=True, max_length=100)),
                ('tl_headertitle', models.CharField(default=b'Surprising Headline Right Here', max_length=100)),
                ('tl_releasetime', models.CharField(default=b'3 hours ago', max_length=20)),
                ('tl_content', models.CharField(default=b'Lorem Ipsum and such.', max_length=1000)),
            ],
        ),
    ]
