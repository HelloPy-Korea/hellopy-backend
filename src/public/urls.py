from django.urls import path

from .views import upload_file

urlpatterns = [
    # Custom upload file endpoint
    path("custom_upload_file/", upload_file, name="custom_upload_file"),
]
