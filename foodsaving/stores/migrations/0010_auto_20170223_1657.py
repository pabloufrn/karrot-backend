# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 16:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0011_auto_20170223_1629'),
        ('stores', '0009_store_deleted'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='store',
            unique_together=set([('group', 'name')]),
        ),
    ]