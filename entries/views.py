from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status, mixins, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from entries.models import Entry
from entries.serializers import EntrySerializer


class EntryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer