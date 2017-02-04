# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_auto_20161211_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickupDateSeries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('max_collectors', models.IntegerField(blank=True, null=True)),
                ('rule', models.TextField()),
                ('start_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='pickupdate',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='pickupdate',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='store',
            name='weeks_in_advance',
            field=models.PositiveIntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='pickupdate',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_dates', to='stores.Store'),
        ),
        migrations.AddField(
            model_name='pickupdateseries',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='stores.Store'),
        ),
        migrations.AddField(
            model_name='pickupdate',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pickup_dates', to='stores.PickupDateSeries'),
        ),
    ]
