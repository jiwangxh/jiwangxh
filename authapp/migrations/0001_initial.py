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
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(unique=True, max_length=40)),
                ('upassword', models.CharField(max_length=40)),
                ('uemail', models.CharField(default=b' ', max_length=35)),
                ('uphone', models.CharField(default=b' ', max_length=11)),
                ('uaddress', models.CharField(default=b' ', max_length=100)),
                ('uicon', models.ImageField(default=b'/media/userinfo/one.png', upload_to=b'userinfo')),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.AddField(
            model_name='role',
            name='user',
            field=models.ForeignKey(to='authapp.UserInfo'),
        ),
    ]
