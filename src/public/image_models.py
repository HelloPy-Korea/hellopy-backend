from datetime import timedelta

from django.db import models

from core.storage import s3_delete_file


class TemporaryImage(models.Model):
    path = models.CharField("임시 저장된 이미지 경로", max_length=255)
    created_at = models.DateTimeField("임시 저장 일시", auto_now_add=True)
    expiry_at = models.DateTimeField(
        "만료 일시",
        db_default=models.functions.TruncDate(
            models.functions.Now() + timedelta(days=1), output_field=models.DateField()
        ),
    )

    class Meta:
        indexes = (models.Index(fields=["path"]),)
        verbose_name = "임시 이미지"
        verbose_name_plural = "임시 이미지들"

    def delete(self, *args, **kwargs) -> None:
        s3_delete_file(self.path)

        super().delete(*args, **kwargs)

    def soft_delete(self, *args, **kwargs) -> None:
        """임시 이미지 삭제"""
        super().delete(*args, **kwargs)
