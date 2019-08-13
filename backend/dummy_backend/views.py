# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from utilities.customperm import Custom

from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import DummySerializer
from .models import Dummy

from rest_framework.response import Response


class DummyView(ModelViewSet):
	authentication_classes = [TokenAuthentication]
	permission_classes = [Custom]


	serializer_class = DummySerializer
	queryset = Dummy.objects.all()
