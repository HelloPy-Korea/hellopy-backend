# models.py
import os

from django.db import models


class PymonCalendar(models.Model):
    year_month = models.DateField(verbose_name="연도-월", null=False, default="2024-01-01")
    description = models.CharField(max_length=100, verbose_name="설명", default="파이몬 설명")
    calendar_photo = models.ImageField(upload_to="calendar/", blank=False, null=False)

    class Meta:
        verbose_name = "이달의 달력"
        verbose_name_plural = "이달의 달력"

    def delete(self, *args, **kwargs):
        # 연결된 이미지 파일 삭제
        if self.calendar_photo and os.path.isfile(self.calendar_photo.path):
            os.remove(self.calendar_photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.year_month)
