# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-29 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20180329_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='song_like',
            name='song_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
