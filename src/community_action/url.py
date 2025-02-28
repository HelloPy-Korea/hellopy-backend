from rest_framework.routers import DefaultRouter

from .views import ActionPhotoViewSet, CommunityActionViewSet, CommunityTagViewSet, TagViewSet

router = DefaultRouter()
router.register(r"community-actions", CommunityActionViewSet)
router.register(r"tags", TagViewSet)
router.register(r"community-tags", CommunityTagViewSet)
router.register(r"action-photos", ActionPhotoViewSet)

urlpatterns = router.urls
