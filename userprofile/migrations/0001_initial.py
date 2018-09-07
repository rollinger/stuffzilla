# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-06 20:33
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('position', '0017_auto_20180906_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Your Photo')),
                ('language', models.CharField(choices=[('en', 'English'), ('de', 'German'), ('pt', 'Portuguese'), ('es', 'Spanish')], help_text='Which language would you like to use?', max_length=255, verbose_name='Application Language')),
                ('phone_number', models.CharField(blank=True, help_text='Your phone number to reach out to you.', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('location', models.OneToOneField(help_text='Your Main Address', on_delete=django.db.models.deletion.PROTECT, related_name='main_address', to='position.Address')),
                ('user', models.OneToOneField(help_text='User Account of this Profile', on_delete=django.db.models.deletion.PROTECT, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]