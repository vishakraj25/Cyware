# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-27 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20180827_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='idd',
            field=models.CharField(default='django', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='information',
            name='login',
            field=models.CharField(default='django', max_length=100),
            preserve_default=False,
        ),
    ]