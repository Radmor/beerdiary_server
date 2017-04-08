# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0002_auto_20170318_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pub',
            name='atmosphere_description',
            field=models.TextField(blank=True, default='', verbose_name='atmosphere description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pub',
            name='city',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='city'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pub',
            name='design_description',
            field=models.TextField(blank=True, default='', verbose_name='design description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pub',
            name='street',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='street'),
            preserve_default=False,
        ),
    ]
