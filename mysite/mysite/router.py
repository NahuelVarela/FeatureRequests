from rest_framework import routers

#Our import
from fr_site.viewsets import FeaturesViewSet

router = routers.DefaultRouter()
router.register(r'featuresitems', FeaturesViewSet, basename='FeaturesViewSet')
urlpatterns = router.urls
