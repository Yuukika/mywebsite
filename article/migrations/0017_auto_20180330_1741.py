# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-30 09:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20180329_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 9, 41, 3, 280613, tzinfo=utc)),
        ),
    ]
