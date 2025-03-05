from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Notice(models.Model):
    title = models.CharField("제목", max_length=255)
    content = CKEditor5Field("본문", config_name="extends")
    is_deleted = models.BooleanField("삭제 여부", default=False)
    is_pinned = models.BooleanField("상단 고정", default=False)
    created_at = models.DateTimeField("등록 일시", auto_now_add=True)
    updated_at = models.DateTimeField("수정 일시", auto_now=True)

    class Meta:
        verbose_name = "notice"
        verbose_name_plural = "공지사항"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Notice(id={self.id}, title={self.title})"
