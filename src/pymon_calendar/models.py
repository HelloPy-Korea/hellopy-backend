# models.py
from django.db import models


class PymonCalendar(models.Model):
    year_month = models.DateField(verbose_name="연도-월", null=False, default="2024-01-01")
    description = models.CharField(max_length=100, verbose_name="설명", default="파이몬 설명")
    calendar_photo = models.ImageField(upload_to="calendar/", blank=False, null=False)

    class Meta:
        verbose_name = "캘린더 관리"
        verbose_name_plural = "캘린더 관리"

    def __str__(self):
        return str(self.year_month)
