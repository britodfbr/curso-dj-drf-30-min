from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer


class ClientViewsSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
