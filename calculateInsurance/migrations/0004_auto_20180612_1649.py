# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-12 16:49
from __future__ import unicode_literals

import calculateInsurance.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculateInsurance', '0003_car_insurance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='insurance',
        ),
        migrations.AddField(
            model_name='car',
            name='insurance_payment_due',
            field=models.IntegerField(default=calculateInsurance.models.premiumForTaxiThirdParty, editable=False),
        ),
        migrations.AddField(
            model_name='car',
            name='insurance_type',
            field=models.CharField(default='third party', max_length=50),
        ),
    ]