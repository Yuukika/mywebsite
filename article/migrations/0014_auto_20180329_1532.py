# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-29 07:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20180329_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 7, 32, 4, 714104, tzinfo=utc)),
        ),
    ]
