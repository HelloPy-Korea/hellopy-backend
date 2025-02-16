from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Notice(models.Model):
    title = models.CharField(max_length=255, verbose_name="제목")
    content = CKEditor5Field("Content", config_name="extends")
    is_deleted = models.BooleanField(default=False, verbose_name="삭제 여부")
    is_pinned = models.BooleanField(verbose_name="고정 여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "공지"
        verbose_name_plural = "공지사항"
    def __str__(self):
        return self.title