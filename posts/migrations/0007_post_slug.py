# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_title_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=500, unique=True), unique=True),
        ),
    ]
