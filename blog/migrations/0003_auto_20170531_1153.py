# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 16:53
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170525_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='preview',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='notes',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
