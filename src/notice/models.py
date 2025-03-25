import os

from bs4 import BeautifulSoup
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from public.tag_models import NoticeTag, Tag


class Notice(models.Model):
    title = models.CharField("제목", max_length=255)
    content = CKEditor5Field("본문", config_name="extends", null=False, blank=False)
    is_deleted = models.BooleanField("삭제 여부", default=False)
    is_pinned = models.BooleanField("상단 고정", default=False)
    created_at = models.DateTimeField("등록 일시", auto_now_add=True)
    updated_at = models.DateTimeField("수정 일시", auto_now=True)
    tag = models.ManyToManyField(Tag, through=NoticeTag, related_name="notice")

    def clean(self):
        # HTML 태그 제거 테스트 추출
        soup = BeautifulSoup(self.content, "html.parser")

        if not soup.get_text(strip=True):
            raise ValidationError({"content": "내용을 입력해주세요."})

    def delete(self, *args, **kwargs):
        self._delete_ckeditor_images()
        super().delete(*args, **kwargs)

    def _delete_ckeditor_images(self):
        soup = BeautifulSoup(self.content, "html.parser")
        for img_tag in soup.find_all("img"):
            src = img_tag.get("src")
            if src and src.startswith(settings.MEDIA_URL + "notice/ckeditor"):
                relative_path = src.replace(settings.MEDIA_URL, "")
                file_path = os.path.join(settings.MEDIA_ROOT, relative_path)
                if os.path.isfile(file_path):
                    os.remove(file_path)

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Notice(id={self.id}, title={self.title})"
