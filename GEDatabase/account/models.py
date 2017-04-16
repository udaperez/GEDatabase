# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import admin

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    year_level = models.IntegerField(default=1)
    year_standing = models.IntegerField(default=1)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Instrument(models.Model):
    STATUS_CHOICES = (
        ('available', 'AVAILABLE'),
        ('on_loan', 'ON LOAN'),
        ('out_of_order', 'OUT OF ORDER'),
    )
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='')
    serial = models.CharField(max_length=250, default='')
    slug = models.SlugField(max_length=250)
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default='AVAILABLE')

    def __str__(self):
        return self.name
    
    def lend(self):
        status = models.CharField(default='ON LOAN')

class LendInstrument(Instrument):
    instrument = Instrument()
    user = models.ForeignKey(Profile, related_name=None)
    if instrument.status == 'AVAILABLE':
        user = models.OneToOneField(settings.AUTH_USER_MODEL)
        instrument.status = 'ON LOAN'