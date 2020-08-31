from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EventSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #url = serializers.HyperlinkedIdentityField(view_name='user-detail', format='html')

    class Meta:
        model = Events
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']