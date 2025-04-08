# models.py

from django.db import models

from public.mixin.img_models import MultiImageFieldMixin


class PymonCalendar(MultiImageFieldMixin):
    year_month = models.DateField(verbose_name="연도-월", null=False, default="2024-01-01")
    description = models.CharField(max_length=100, verbose_name="설명", default="파이몬 설명")
    calendar_photo = models.ImageField(upload_to="calendar/", blank=False, null=False)

    # MultiImageFieldMixin에서 clean, delete를 위해 필요한 정보 작성
    image_field_names = ["calendar_photo"]

    class Meta:
        verbose_name = "이달의 달력"
        verbose_name_plural = "이달의 달력"

    def __str__(self):
        return str(self.year_month)
