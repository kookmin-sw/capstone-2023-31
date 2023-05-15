import json
from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from rest_framework import generics

from .models import Glasses
from .serializers import PostSerializer

class ListPost(generics.ListCreateAPIView):
    queryset = Glasses.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateAPIView):
    queryset = Glasses.objects.all()
    serializer_class = PostSerializer