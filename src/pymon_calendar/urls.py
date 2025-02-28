from rest_framework.routers import DefaultRouter

from .views import PymonCalendarViewSet

router = DefaultRouter()
router.register(r"", PymonCalendarViewSet, basename="calendar")

urlpatterns = router.urls
