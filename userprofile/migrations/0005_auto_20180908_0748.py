# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 07:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20180908_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='owner',
        ),
    ]
