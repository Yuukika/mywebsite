# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-30 16:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20180330_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 16, 13, 20, 468436, tzinfo=utc)),
        ),
    ]