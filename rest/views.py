from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest.models import Quote
from rest.serializers import QuoteSerializers


class Quotes(viewsets.ModelViewSet):
    serializer_class = QuoteSerializers
    queryset = Quote.objects.all()