from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'dataqrfiles',DataQRFileViewSet,basename='dataqrfile')


urlpatterns = router.urls
