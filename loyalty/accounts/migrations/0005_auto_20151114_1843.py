# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-14 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='webhook',
            new_name='webhook_id',
        ),
    ]