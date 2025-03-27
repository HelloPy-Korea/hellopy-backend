import os

from django.core.exceptions import ValidationError


class ImageFieldMixin:
    """
    - 이미지 필드 유효성 검사 (`clean`)
    - 삭제 시 이미지 파일 제거 (`delete`)
    모델 클래스에서 `image_field_name`을 설정해 주세요. 기본값은 'image'입니다.
    """

    image_field_name = "image"

    def clean(self):
        super().clean()
        image_field = getattr(self, self.image_field_name, None)
        if not image_field or not getattr(image_field, "name", None):
            raise ValidationError(
                {self.image_field_name: "이미지 파일을 반드시 업로드해야 합니다."}
            )

    def delete(self, *args, **kwargs):
        image_field = getattr(self, self.image_field_name, None)
        if image_field and hasattr(image_field, "path"):
            image_path = image_field.path
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)

    class Meta:
        abstract = True
