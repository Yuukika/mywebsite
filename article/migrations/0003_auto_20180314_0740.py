# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-14 07:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180314_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 14, 7, 40, 30, 62632, tzinfo=utc)),
        ),
    ]
