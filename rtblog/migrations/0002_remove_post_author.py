# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-14 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
