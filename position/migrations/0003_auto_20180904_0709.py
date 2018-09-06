# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-04 07:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('position', '0002_auto_20180901_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='user',
            field=models.ForeignKey(blank=True, help_text='User creating the Address', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to=settings.AUTH_USER_MODEL),
        ),
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
