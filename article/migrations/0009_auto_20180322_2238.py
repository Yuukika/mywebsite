# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-22 14:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20180322_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 22, 14, 38, 17, 464774, tzinfo=utc)),
        ),
    ]
