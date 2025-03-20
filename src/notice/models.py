from django.core.exceptions import ValidationError
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from public.models import NoticeTag, Tag


class Notice(models.Model):
    title = models.CharField("제목", max_length=255)
    content = CKEditor5Field("본문", config_name="extends", null=False, blank=False)
    is_deleted = models.BooleanField("삭제 여부", default=False)
    is_pinned = models.BooleanField("상단 고정", default=False)
    created_at = models.DateTimeField("등록 일시", auto_now_add=True)
    updated_at = models.DateTimeField("수정 일시", auto_now=True)
    tag = models.ManyToManyField(Tag, through=NoticeTag, related_name="notice")

    def clean(self):
        from bs4 import BeautifulSoup

        # HTML 태그 제거 테스트 추출
        soup = BeautifulSoup(self.content, "html.parser")

        if not soup.get_text(strip=True):
            raise ValidationError({"content": "내용을 입력해주세요."})

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Notice(id={self.id}, title={self.title})"
