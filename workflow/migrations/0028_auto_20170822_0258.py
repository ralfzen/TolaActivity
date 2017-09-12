# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0027_workflowlevel2sort_workflowlevel2_parent_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TolaUserFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_filter', models.DateField(blank=True, null=True)),
                ('end_date_filter', models.DateField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('country_filter', models.ManyToManyField(blank=True, related_name='filter_country', to='workflow.Country')),
                ('sector_filter', models.ManyToManyField(blank=True, related_name='filter_sector', to='workflow.Sector')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter_user', to='workflow.TolaUser')),
                ('workflowlevel1_filter', models.ManyToManyField(blank=True, related_name='filter_level1', to='workflow.WorkflowLevel1')),
                ('workflowlevel2_filter', models.ManyToManyField(blank=True, related_name='filter_level2', to='workflow.WorkflowLevel2')),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.AlterField(
            model_name='workflowmodules',
            name='modules',
            field=models.CharField(choices=[('approval', 'Approval'), ('budget', 'Budget'), ('stakeholders', 'Stakeholders'), ('documents', 'Documents'), ('sites', 'Sites'), ('indicators', 'Indicators')], default='open', max_length=50),
        ),
    ]