from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=255, verbose_name="삭제 여부")
    content = models.TextField(verbose_name="내용")
    is_deleted = models.BooleanField(verbose_name="삭제 여부")
    is_pinned = models.BooleanField(default=False, verbose_name="고정 여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "공지"
        verbose_name_plural = "공지사항"
    def __str__(self):
        return self.title