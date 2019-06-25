from django.contrib.auth.models import User, Group
from rest_framework import serializers

#Our imports
from .models import FeaturesItems

class FeaturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeaturesItems
        fields = ('owner', 'handler', 'status', 'title', 'description', 'last_modify_date', 'created_date')