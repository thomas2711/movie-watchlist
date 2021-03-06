# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 05:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('year', models.PositiveSmallIntegerField(default=0)),
                ('rt_rating', models.IntegerField(default=0)),
                ('watched', models.BooleanField(default=False)),
                ('tmdb_id', models.IntegerField(default=0)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_watched', models.DateField(default=datetime.date.today)),
                ('poster_url', models.CharField(max_length=200)),
            ],
        ),
    ]
