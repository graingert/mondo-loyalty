# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-15 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_loyaltyschemelink_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotifiedTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mondo_transaction_id', models.CharField(max_length=50)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notified_transactions', to='accounts.LoyaltySchemeLink')),
            ],
        ),
    ]
