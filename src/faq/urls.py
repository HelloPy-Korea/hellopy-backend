from rest_framework.routers import DefaultRouter

from .views import FAQViewSet

router = DefaultRouter()
router.register(r'', FAQViewSet, basename="faq")  # 'faqs' 대신 빈 문자열

urlpatterns = router.urls
