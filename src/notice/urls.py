from rest_framework.routers import DefaultRouter

from .views import NoticeViewSet

router = DefaultRouter()
router.register("", NoticeViewSet, basename="notice")

urlpatterns = router.urls
