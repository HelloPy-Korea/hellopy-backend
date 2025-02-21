from rest_framework.routers import DefaultRouter
from .views import MdViewSet

"""
GET /md/ → 모든 Md 객체 목록 조회 ✅
GET /md/{id}/ → 특정 Md 객체 조회 ✅
"""

router = DefaultRouter()
router.register(r'', MdViewSet, basename="md")

urlpatterns = router.urls