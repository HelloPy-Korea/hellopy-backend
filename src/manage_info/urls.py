from rest_framework.routers import DefaultRouter

from .views import ManagementInfoViewSet

router = DefaultRouter()
router.register(r"", ManagementInfoViewSet)

urlpatterns = router.urls
