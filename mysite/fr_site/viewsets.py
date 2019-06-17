from rest_framework import viewsets

from .serializers import FeaturesSerializer
from .models import FeaturesItems

class FeaturesViewSet(viewsets.ModelViewSet):

	queryset = FeaturesItems.objects.all()
	serializer_class = FeaturesSerializer