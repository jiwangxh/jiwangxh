# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('rid', models.IntegerField(serialize=False, primary_key=True)),
                ('rname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upassword', models.CharField(max_length=40)),
                ('uemail', models.CharField(default=b'', max_length=20)),
                ('uphone', models.CharField(default=b'', max_length=11)),
                ('uaddress', models.CharField(default=b'', max_length=100)),
                ('uicon', models.ImageField(default=b'', upload_to=b'userinfo')),
                ('urole', models.ForeignKey(to='authapp.Role')),
            ],
        ),
    ]
