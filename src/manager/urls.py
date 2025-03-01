from rest_framework.routers import DefaultRouter

from .views import ManagerViewSet

router = DefaultRouter()
router.register("", ManagerViewSet, basename="manager")

urlpatterns = router.urls
