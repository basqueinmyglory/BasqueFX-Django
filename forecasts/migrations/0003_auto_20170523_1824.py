# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasts', '0002_auto_20170523_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('currency', models.TextField(blank=True, db_column='Currency', null=True)),
                ('event', models.TextField(blank=True, db_column='Event', null=True)),
                ('impact', models.TextField(blank=True, db_column='Impact', null=True)),
                ('time_eastern', models.TextField(blank=True, db_column='Time_Eastern', null=True)),
                ('forecast', models.TextField(blank=True, db_column='Forecast', null=True)),
                ('previous', models.TextField(blank=True, db_column='Previous', null=True)),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
        migrations.RenameField(
            model_name='dailyforecast',
            old_name='pub_date',
            new_name='entry_date',
        ),
    ]