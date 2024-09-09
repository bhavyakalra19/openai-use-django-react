from rest_framework import serializers
from .models import *

class DestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationData
        fields = '__all__'
