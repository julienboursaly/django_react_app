# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Dummy(models.Model):
    name = models.CharField(max_length=120, default="DummyObject")
    data = models.CharField(max_length=120)

    def _str_(self):
        return self.name
