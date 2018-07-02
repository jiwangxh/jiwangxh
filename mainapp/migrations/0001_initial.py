# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentManage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Featurette',
            fields=[
                ('ft_id', models.IntegerField(serialize=False, primary_key=True)),
                ('ft_name', models.CharField(unique=True, max_length=10)),
                ('ft_title', models.CharField(max_length=20)),
                ('ft_content', models.TextField(default=b'Nothing there Nothing there Nothing there Nothing there Nothing there Nothing there')),
                ('ft_images', models.ImageField(upload_to=b'featurette')),
            ],
            options={
                'db_table': 'featurette',
            },
        ),
        migrations.CreateModel(
            name='GlobalAdvert',
            fields=[
                ('ga_id', models.IntegerField(serialize=False, primary_key=True)),
                ('ga_name', models.CharField(unique=True, max_length=10)),
                ('ga_images', models.ImageField(default=b'', upload_to=b'globaladvert')),
                ('ga_content', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'globaladvert',
            },
        ),
        migrations.CreateModel(
            name='GlobalManage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gm_globaladvert', models.ForeignKey(to='mainapp.GlobalAdvert')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalTitle',
            fields=[
                ('gt_id', models.IntegerField(serialize=False, primary_key=True)),
                ('gt_name', models.CharField(unique=True, max_length=10)),
                ('gt_logo', models.ImageField(default=b'', upload_to=b'globaltitle')),
                ('gt_content', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'globaltitle',
            },
        ),
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hc_advert', models.ForeignKey(to='mainapp.GlobalAdvert')),
                ('hc_featurette', models.ForeignKey(to='mainapp.Featurette')),
            ],
        ),
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('mt_id', models.IntegerField(serialize=False, primary_key=True)),
                ('mt_name', models.CharField(unique=True, max_length=10)),
                ('mt_title', models.CharField(max_length=20)),
                ('mt_content', models.TextField(default=b'Nothing there Nothing there Nothing there Nothing there Nothing there Nothing there')),
                ('mt_icon', models.ImageField(default=b'', upload_to=b'marketing')),
                ('mt_images', models.ImageField(default=b'', upload_to=b'marketing')),
            ],
            options={
                'db_table': 'marketing',
            },
        ),
        migrations.CreateModel(
            name='PageManage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLbum',
            fields=[
                ('pl_id', models.IntegerField(serialize=False, primary_key=True)),
                ('pl_name', models.CharField(unique=True, max_length=10)),
                ('pl_title', models.CharField(max_length=100)),
                ('pl_images', models.ImageField(upload_to=b'photolbum')),
            ],
            options={
                'db_table': 'photolbum',
            },
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='hc_marketing',
            field=models.ForeignKey(to='mainapp.Marketing'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='hc_photolbum',
            field=models.ForeignKey(to='mainapp.PhotoLbum'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='hc_title',
            field=models.ForeignKey(to='mainapp.GlobalTitle'),
        ),
        migrations.AddField(
            model_name='globalmanage',
            name='gm_globaltitle',
            field=models.ForeignKey(to='mainapp.GlobalTitle'),
        ),
    ]
