# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-30 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activitydb', '0011_auto_20160630_1217'),
        ('indicators', '0003_auto_20160613_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaggregationtype',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.Country'),
        ),
        migrations.AddField(
            model_name='disaggregationtype',
            name='standard',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='collecteddata',
            name='update_count_tola_table',
            field=models.BooleanField(default=False, verbose_name=b'Would you like to update the achieved total with the row count from TolaTables?'),
        ),
        migrations.AlterField(
            model_name='historicalcollecteddata',
            name='update_count_tola_table',
            field=models.BooleanField(default=False, verbose_name=b'Would you like to update the achieved total with the row count from TolaTables?'),
        ),
    ]