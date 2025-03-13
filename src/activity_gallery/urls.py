from rest_framework.routers import DefaultRouter

from .views import ActivityActionViewSet

router = DefaultRouter()
router.register("", ActivityActionViewSet, basename="activity-action")

urlpatterns = router.urls
