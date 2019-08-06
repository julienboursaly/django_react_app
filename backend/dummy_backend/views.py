# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DummySerializer
from .models import Dummy


class DummyView(viewsets.ModelViewSet):
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
