# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
# from rest_framework import routers, serializers, viewsets
from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
