from rest_framework.routers import DefaultRouter

from .views import MerchandiseViewSet

router = DefaultRouter()
router.register(r"", MerchandiseViewSet, basename="merchandise")

urlpatterns = router.urls
