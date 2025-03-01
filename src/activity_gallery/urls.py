from rest_framework.routers import DefaultRouter

from .views import ActivityActionViewSet

router = DefaultRouter()
router.register(r"activity-actions", ActivityActionViewSet, basename="activity-action")

urlpatterns = router.urls
