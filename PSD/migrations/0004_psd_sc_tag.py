# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSD', '0003_auto_20160613_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='psd',
            name='sc_tag',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
