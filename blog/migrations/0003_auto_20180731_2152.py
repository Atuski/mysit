# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180725_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time'], 'verbose_name': '博客', 'verbose_name_plural': '博客'},
        ),
    ]