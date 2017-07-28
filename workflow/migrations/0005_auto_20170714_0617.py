# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0004_auto_20170713_0518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workflowaccess',
            options={'ordering': ('workflow_user',), 'verbose_name_plural': 'WorkflowAccess'},
        ),
        migrations.RenameField(
            model_name='workflowaccess',
            old_name='approval_user',
            new_name='workflow_user',
        ),
        migrations.AddField(
            model_name='historicalworkflowlevel2',
            name='project_activity',
            field=models.CharField(blank=True, help_text='This should come directly from the activities listed in the Logframe', max_length=255, null=True, verbose_name='Project Activity'),
        ),
        migrations.AddField(
            model_name='historicalworkflowlevel2',
            name='project_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.ProjectType'),
        ),
        migrations.AddField(
            model_name='workflowaccess',
            name='role',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workflowlevel2',
            name='project_activity',
            field=models.CharField(blank=True, help_text='This should come directly from the activities listed in the Logframe', max_length=255, null=True, verbose_name='Project Activity'),
        ),
        migrations.AddField(
            model_name='workflowlevel2',
            name='project_type',
            field=models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.ProjectType', verbose_name='Project Type'),
        ),
    ]