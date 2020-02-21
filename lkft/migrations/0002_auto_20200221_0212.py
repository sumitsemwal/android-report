# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-02-21 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lkft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('number_passed', models.IntegerField()),
                ('number_failed', models.IntegerField()),
                ('number_total', models.IntegerField()),
                ('modules_done', models.IntegerField()),
                ('modules_total', models.IntegerField()),
                ('started_at', models.DateTimeField(null=True)),
                ('fetched_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cibuild',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cibuild',
            name='result',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cibuild',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cibuild',
            name='kernel_change',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lkft.KernelChange'),
        ),
        migrations.AddField(
            model_name='reportbuild',
            name='ci_build',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ci_build', to='lkft.CiBuild'),
        ),
        migrations.AddField(
            model_name='reportbuild',
            name='ci_trigger_build',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trigger_build', to='lkft.CiBuild'),
        ),
        migrations.AddField(
            model_name='reportbuild',
            name='kernel_change',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lkft.KernelChange'),
        ),
    ]
