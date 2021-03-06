# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 08:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('brand', models.CharField(default='', max_length=250)),
                ('serial', models.CharField(default='', max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('status', models.CharField(choices=[('available', 'AVAILABLE'), ('on_loan', 'ON LOAN'), ('out_of_order', 'OUT OF ORDER')], default='AVAILABLE', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_level', models.IntegerField(default=1)),
                ('year_standing', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LendInstrument',
            fields=[
                ('instrument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.Instrument')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('account.instrument',),
        ),
    ]
