# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-03 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import pipeline.engine.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0024_auto_20200224_0308"),
    ]

    operations = [
        migrations.CreateModel(
            name="MultiCallbackData",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="自增ID")),
                ("schedule_id", models.CharField(max_length=64, verbose_name="回调服务ID")),
                ("data", pipeline.engine.models.fields.IOField(verbose_name="回调数据")),
            ],
        ),
    ]
