# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-06 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stuff',
            options={'ordering': ['-created_at'], 'verbose_name': 'Stuff', 'verbose_name_plural': 'Stuff'},
        ),
        migrations.AlterField(
            model_name='stuff',
            name='description',
            field=models.TextField(blank=True, help_text='Long Description of the Item, Service or Event (max. 2000 characters)', max_length=2000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stuff/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='title',
            field=models.CharField(help_text='Title Description of the Item, Service or Event (max. 255 characters)', max_length=255, verbose_name='Title'),
        ),
    ]