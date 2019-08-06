# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Dummy


class DummyBackendAdmin(admin.ModelAdmin):
    list_display = ('name', 'data')


# Register your models here.
admin.site.register(Dummy, DummyBackendAdmin)
