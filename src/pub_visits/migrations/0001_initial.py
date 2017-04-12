# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pubs', '0003_auto_20170320_1915'),
        ('beers', '0002_auto_20170320_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('beer', models.ManyToManyField(to='beers.Beer', verbose_name='beer')),
                ('pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pubvisits', to='pubs.Pub', verbose_name='pub')),
            ],
            options={
                'verbose_name_plural': 'Pub visits',
                'verbose_name': 'Pub visit',
            },
        ),
    ]
