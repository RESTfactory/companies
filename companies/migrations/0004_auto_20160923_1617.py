# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20160923_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationalunit',
            name='unit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit', to='companies.OrganizationalUnitType'),
        ),
    ]
