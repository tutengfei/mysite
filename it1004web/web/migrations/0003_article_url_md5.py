# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_article_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url_md5',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, validators='链接的MD5'),
        ),
    ]
