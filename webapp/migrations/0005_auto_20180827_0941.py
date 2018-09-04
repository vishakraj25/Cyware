# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-27 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180827_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='avatar_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='bio',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='blog',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='created_at',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='email',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='events_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='followers',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='followers_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='following',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='following_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='gists_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='gravatar_id',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='hireable',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='html_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='idd',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='location',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='login',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='name',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='organizations_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='public_gists',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='public_repos',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='received_events_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='repos_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='site_admin',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='starred_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='subscriptions_url',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='typ',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='updated_at',
            field=models.CharField(default='nll', max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='url',
            field=models.CharField(default='nll', max_length=100),
        ),
    ]
