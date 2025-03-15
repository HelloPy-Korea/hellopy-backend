from django.core.exceptions import ValidationError
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from core.mixins.models import SoftDeleteModel


class Notice(SoftDeleteModel):
    title = models.CharField("제목", max_length=255)
    content = CKEditor5Field("본문", config_name="extends", null=False, blank=False)
    is_pinned = models.BooleanField("상단 고정", default=False)
    created_at = models.DateTimeField("등록 일시", auto_now_add=True)
    updated_at = models.DateTimeField("수정 일시", auto_now=True)

    def clean(self):
        super().clean()
        if self.content.strip() in (
            "",
            "<p>&nbsp;</p>",
            "<p>&nbsp;</p><p>&nbsp;</p>",
            "<p>&nbsp;&nbsp;</p>",
            "<p><br></p>",
        ):
            raise ValidationError({"content": "내용을 입력해주세요."})

    class Meta:
        verbose_name = "notice"
        verbose_name_plural = "공지사항"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Notice(id={self.id}, title={self.title})"
