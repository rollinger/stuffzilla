# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 11:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0041_auto_20180908_0748'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='area',
            unique_together=set([]),
        ),
    ]
