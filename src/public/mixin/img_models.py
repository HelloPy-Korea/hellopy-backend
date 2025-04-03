from pathlib import Path

from django.core.exceptions import ValidationError
from django.db import models


class MultiImageFieldMixin(models.Model):
    """
    다중 이미지 필드를 사용하는 Django 모델에서 이미지 파일의 유효성 검사 및 파일 삭제를 자동으로 처리하는 Mixin입니다.

    사용 방법:
    - `image_field_names` 클래스 속성에 이미지 필드 이름들을 리스트 형태로 지정하세요.
      예: image_field_names = ["image", "thumbnail"]

    기능:
    1. clean(): 각 이미지 필드에 유효한 이미지가 업로드되었는지 검사합니다.
       (비어 있으면 ValidationError 발생)

    2. delete(): 모델 인스턴스 삭제 시, 지정된 모든 이미지 필드의 실제 파일도 파일 시스템에서 삭제합니다.

    주의:
    - 이 Mixin은 abstract 모델로 사용되어야 하며, 직접 테이블로 생성되지 않습니다.
    """

    # 이미지 필드가 여러 개가 될 경우를 추가하기 위해 리스트로 변경
    image_field_names = []

    # 이미지 필드가 비어있는 경우 검증이 되지 않아 이미지가 없는 경우 ValidationError 발생
    def clean(self):
        super().clean()
        for field_name in self.image_field_names:
            image_field = getattr(self, field_name, None)
            if not image_field or not getattr(image_field, "name", None):
                raise ValidationError(
                    {field_name: f"{field_name} 필드는 반드시 이미지를 포함해야 합니다."}
                )

    def delete(self, *args, **kwargs):
        for field_name in self.image_field_names:
            image_field = getattr(self, field_name, None)
            if image_field and hasattr(image_field, "path"):
                image_path = Path(image_field.path)
                if image_path.is_file():
                    image_path.unlink()
        super().delete(*args, **kwargs)

    class Meta:
        abstract = True
