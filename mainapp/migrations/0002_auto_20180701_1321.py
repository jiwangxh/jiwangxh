# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globaladvert',
            name='ga_logo',
        ),
        migrations.AddField(
            model_name='globaladvert',
            name='ga_images',
            field=models.ImageField(default=b'', upload_to=b'globaladvert'),
        ),
        migrations.AlterField(
            model_name='globaltitle',
            name='gt_logo',
            field=models.ImageField(default=b'', upload_to=b'globaltitle'),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='mt_icon',
            field=models.ImageField(default=b'', upload_to=b'marketing'),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='mt_images',
            field=models.ImageField(default=b'', upload_to=b'marketing'),
        ),
    ]
