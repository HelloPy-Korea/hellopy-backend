from bs4 import BeautifulSoup
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_ckeditor_5.signals import extract_image_paths

from core.mixins.models import SoftDeleteModel
from core.storage import s3_delete_file
from public.tag_models import NoticeTag, Tag


class Notice(SoftDeleteModel):
    title = models.CharField("제목", max_length=255)
    content = CKEditor5Field("본문", config_name="extends", null=False, blank=False)
    is_pinned = models.BooleanField("상단 고정", default=False)
    is_visible = models.BooleanField("공지사항 공개 여부", default=True)
    created_at = models.DateTimeField("등록 일시", auto_now_add=True)
    updated_at = models.DateTimeField("수정 일시", auto_now=True)
    tags = models.ManyToManyField(Tag, through=NoticeTag, related_name="notice")

    def clean(self):
        # HTML 태그 제거 테스트 추출
        soup = BeautifulSoup(self.content, "html.parser")

        if not soup.get_text(strip=True):
            raise ValidationError({"content": "내용을 입력해주세요."})

    def delete(self, *args, **kwargs):
        self._delete_ckeditor_images()
        super().delete(*args, **kwargs)

    def _delete_ckeditor_images(self):
        images_to_delete = extract_image_paths(self.content)
        try:
            for img_path in images_to_delete:
                # CKEditor5Field의 이미지 경로는 상대 경로이므로, 절대 경로로 변환
                file_path = img_path.removeprefix(f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/")
                s3_delete_file(file_path)
        except Exception as e:
            raise ValidationError(f"이미지 삭제 오류: {e}")

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Notice(id={self.id}, title={self.title})"
