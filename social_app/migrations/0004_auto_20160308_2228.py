# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 22:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_app', '0003_auto_20160308_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='likes',
        ),
        migrations.AddField(
            model_name='topic',
            name='likes',
            field=models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
