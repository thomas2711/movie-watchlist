# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 02:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170817_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date_watched',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]