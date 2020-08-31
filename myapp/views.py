from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly
from rest_framework import renderers, viewsets
from .serializers import *


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    