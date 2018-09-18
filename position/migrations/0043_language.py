# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-11 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0042_auto_20180908_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Standard language code representation. Ex.: en_AU', max_length=10, verbose_name='Language Code')),
                ('name', models.CharField(help_text='Name of the Language. Ex.: English', max_length=100, verbose_name='Language Name')),
                ('country', models.CharField(help_text='Name of the Country. Ex.: Australia', max_length=100, verbose_name='Country')),
                ('supported', models.BooleanField(default=False, help_text='If the language is supported in the App Translation Sytem', verbose_name='Translation supported')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Language',
                'ordering': ['name', 'country'],
            },
        ),
    ]