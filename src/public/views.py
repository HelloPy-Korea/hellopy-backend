from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_POST
from django_ckeditor_5.exceptions import NoImageException
from django_ckeditor_5.forms import UploadFileForm
from django_ckeditor_5.permissions import check_upload_permission
from django_ckeditor_5.storage_utils import get_django_storage_class, image_verify

from .image_models import TemporaryImage


def handle_uploaded_file(f, path):
    storage = get_django_storage_class()
    fs = storage()
    filename = fs.save(path, f)
    return fs.url(filename)


@require_POST
@check_upload_permission
def upload_file(request: HttpRequest) -> JsonResponse:
    form = UploadFileForm(request.POST, request.FILES)
    allow_all_file_types = getattr(settings, "CKEDITOR_5_ALLOW_ALL_FILE_TYPES", False)
    upload_image = request.FILES.get("upload", None)

    if not allow_all_file_types:
        try:
            image_verify(upload_image)
        except NoImageException as ex:
            return JsonResponse({"error": {"message": f"{ex}"}}, status=400)

    if form.is_valid():
        # ckeditor5를 통해 업로드한 파일이 특정 디렉토리에 저장되도록 설정
        directory_prefix = getattr(settings, "CKEDITOR_5_UPLOAD_DIRECTORY_PREFIX", "editor/")
        directory_prefix = directory_prefix.removeprefix("/")
        if not directory_prefix.endswith("/"):
            directory_prefix += "/"
        print(f"Upload image name: {upload_image.name}")
        url = handle_uploaded_file(upload_image, directory_prefix + upload_image.name)
        saved_image_path = url.removeprefix(f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/")
        TemporaryImage.objects.create(path=saved_image_path)
        return JsonResponse({"url": url})

    if form.errors["upload"]:
        return JsonResponse(
            {"error": {"message": form.errors["upload"][0]}},
            status=400,
        )

    return JsonResponse({"error": {"message": "Invalid form data"}}, status=400)
