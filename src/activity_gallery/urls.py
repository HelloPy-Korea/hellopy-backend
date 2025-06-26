from rest_framework.routers import DefaultRouter

from .views import ActivityActionViewSet, ActivityHistoryViewSet

router = DefaultRouter()
router.register("histories", ActivityHistoryViewSet, basename="activity-history")
router.register("", ActivityActionViewSet, basename="activity-action")

urlpatterns = router.urls
