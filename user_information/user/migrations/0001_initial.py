# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-02 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=264, unique=True)),
                ('Last_Name', models.CharField(max_length=264, unique=True)),
                ('Email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
