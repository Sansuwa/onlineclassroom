# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 09:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0005_auto_20171008_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='username',
        ),
        migrations.AddField(
            model_name='course',
            name='course_logo',
            field=models.FileField(default=1, upload_to=''),
        ),
        migrations.AddField(
            model_name='instructor',
            name='information',
            field=models.CharField(default=1, max_length=1000),
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]