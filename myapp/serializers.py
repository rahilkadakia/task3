from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'