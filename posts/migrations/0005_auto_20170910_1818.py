# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170910_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield'),
        ),
    ]