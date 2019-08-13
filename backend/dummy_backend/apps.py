# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps, AppConfig
from django.contrib import admin


class DummyBackendConfig(AppConfig):
    name = 'dummy_backend'


    def ready(self):
        models = apps.get_models()
        for model in models:
            try:
                admin.site.register(model)
            except admin.sites.AlreadyRegistered:
                pass