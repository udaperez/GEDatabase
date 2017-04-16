# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Instrument, LendInstrument

class RegisterInstrument(admin.ModelAdmin):
    list_display = ('name','brand','serial','status')
    list_filter = ('status','name')
    search_fields = ('name','brand','status')
    prepopulated_fields = {'slug':('name','brand','serial',)}
admin.site.register(Instrument, RegisterInstrument)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'year_level', 'year_standing')
    list_filter = ('year_standing','year_level')
admin.site.register(Profile, ProfileAdmin)

class AdminLendInstrument(admin.ModelAdmin):
    list_display = ('name','brand','serial','user')
    list_filter = ('name',)
    search_fields = ('name','brand')
    prepopulated_fields = {'slug':('name','brand','serial',)}
admin.site.register(LendInstrument, AdminLendInstrument)