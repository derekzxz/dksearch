# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
