from rest_framework import viewsets

from .serializers import FeaturesSerializer
from .models import FeaturesItems

class FeaturesViewSet(viewsets.ModelViewSet):
	serializer_class = FeaturesSerializer

	def get_queryset(self):
		status = self.request.query_params.get('status')
		if not status:
			queryset = FeaturesItems.objects.all()
		else:
			queryset = FeaturesItems.objects.filter(status=status)
		return queryset