# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luke', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='summary',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
