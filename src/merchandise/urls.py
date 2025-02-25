from rest_framework.routers import DefaultRouter

from .views import MerchandiseViewSet

"""
GET /Merchandise/ → 모든 Md 객체 목록 조회 ✅
GET /Merchandise/{id}/ → 특정 Md 객체 조회 ✅
"""

router = DefaultRouter()
router.register(r'', MerchandiseViewSet, basename="merchandise")

urlpatterns = router.urls