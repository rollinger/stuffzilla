# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 06:41
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '__first__'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalProfile',
            fields=[
                ('owner', models.OneToOneField(help_text='User Account of this Internal Profile', on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='internal_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('current_subscription_type', models.PositiveSmallIntegerField(choices=[(0, 'No Account'), (1, 'Free Account'), (2, 'Paid Account')], default=1, help_text='Free or Paid Account', verbose_name='Type of current subscribtion')),
                ('subscription_from', models.DateTimeField(blank=True, null=True, verbose_name='Starting Date & Time of current subscription')),
                ('subscription_to', models.DateTimeField(blank=True, null=True, verbose_name='Ending Date & Time of current subscription')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Internal Profile',
                'verbose_name_plural': 'Internal Profiles',
            },
        ),
        migrations.CreateModel(
            name='PrivateProfile',
            fields=[
                ('owner', models.OneToOneField(help_text='User Account of this Private Profile', on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='private_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(help_text='Your email address to reach out to you.', max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, help_text='Your phone number to reach out to you.', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('email_reminder', models.BooleanField(default=True, help_text='If you want a notification per Email about what other people offer and search in your area', verbose_name='Email Reminder')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('app_lang', models.ForeignKey(blank=True, help_text='Which language would you like to use in the App?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_profiles', to='utils.Language')),
                ('current_area', models.ForeignKey(blank=True, help_text='Area you currently are observing', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='utils.Area')),
                ('main_address', models.OneToOneField(blank=True, help_text='Your Main Address', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='main_address', to='utils.Address')),
            ],
            options={
                'verbose_name': 'Private Profile',
                'verbose_name_plural': 'Private Profiles',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('owner', models.OneToOneField(help_text='User Account of this Public Profile', on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='public_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, help_text='How other Users see you.', null=True, upload_to='profile/', verbose_name='Your Photo')),
                ('bio', models.TextField(blank=True, help_text='Say something about yourself.', max_length=1000, null=True, verbose_name='Short Bio')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Public Profile',
                'verbose_name_plural': 'Public Profiles',
            },
        ),
    ]
