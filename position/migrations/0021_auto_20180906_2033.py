# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-06 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0020_auto_20180906_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(help_text='', max_length=255, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_number',
            field=models.CharField(help_text='', max_length=55, verbose_name='Street Number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='supplement',
            field=models.CharField(blank=True, help_text='', max_length=255, null=True, verbose_name='Address Supplements'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(blank=True, help_text='', max_length=55, null=True, verbose_name='Zip Code'),
        ),
    ]
