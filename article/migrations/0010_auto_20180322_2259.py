# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-22 14:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20180322_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 22, 14, 59, 32, 728201, tzinfo=utc)),
        ),
    ]