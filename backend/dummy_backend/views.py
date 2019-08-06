# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import DummySerializer
from .models import Dummy


class DummyView(ModelViewSet):
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
