# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20170606_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
