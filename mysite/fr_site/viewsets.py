from rest_framework import viewsets

from .serializers import FeaturesSerializer
from .models import FeaturesItems

class FeaturesViewSet(viewsets.ModelViewSet):
	serializer_class = FeaturesSerializer

	def get_queryset(self):
		#status = self.request.query_params.get('status')
		fr_id = self.request.query_params.get('id')
		
		if fr_id:
				queryset = FeaturesItems.objects.filter(id = fr_id)
		#if status:
		#		queryset = FeaturesItems.objects.filter(status = status)
		else:
			queryset = FeaturesItems.objects.all()
		return queryset