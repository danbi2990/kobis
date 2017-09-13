# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 01:59
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobis', '0003_auto_20170831_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='companys',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='movies',
            name='directors',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movieCd',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movieNm',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movieNmEn',
            field=models.TextField(),
        ),
    ]