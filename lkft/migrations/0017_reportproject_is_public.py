# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-04-06 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lkft', '0016_auto_20210406_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportproject',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
