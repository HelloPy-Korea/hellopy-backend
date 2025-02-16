from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CKEditorUploadView, NoticeViewSet

router = DefaultRouter()
router.register(r'', NoticeViewSet, basename="notice")

urlpatterns = [
    path("ckeditor/upload/", CKEditorUploadView.as_view(), name="ckeditor_upload"),  # CKEditor 5 업로드 URL 추가
    path("ckeditor5/", include("django_ckeditor_5.urls")),  # CKEditor 5 URL 포함
]
urlpatterns += router.urls