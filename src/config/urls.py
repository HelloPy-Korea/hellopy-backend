"""
URL 패턴 구성
URL의 경로를 입력
기본 각 app의 include("각 app의 urls.py 주소")

"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor5/", include("django_ckeditor_5.urls")),  # ckeditor5
    path("api/faqs/", include("faq.urls")),
    path("api/merchandise/", include("merchandise.urls")),
    path("api/notice/", include("notice.urls")),
    path("api/calendar/", include("pymon_calendar.urls")),
    path("api/manager", include("manager.urls")),
    path("api/activity-gallery/", include("activity_gallery.urls")),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

# 개발 환경에서만 Swagger 및 Redoc 활성화
if settings.DEBUG:
    from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularRedocView,
        SpectacularSwaggerView,
    )

    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
