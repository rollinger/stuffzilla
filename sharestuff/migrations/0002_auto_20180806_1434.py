# Generated by Django 2.0.3 on 2018-08-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharestuff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuff',
            name='location',
        ),
        migrations.AddField(
            model_name='stuff',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='stuff',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='stuff',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stuff',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stuff',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Street'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
