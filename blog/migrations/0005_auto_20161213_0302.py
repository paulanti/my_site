# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161213_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
