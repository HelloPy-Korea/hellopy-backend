from django.contrib import admin

from .models import PymonCalendar

# Register your models here.


@admin.register(PymonCalendar)
class PymonCalendarAdmin(admin.ModelAdmin):
    list_display = ("year_month", "description", "calendar_photo")
    search_fields = ("year_month", "description")  # 검색 가능 필드
    list_filter = ("year_month",)  # 필터 옵션
    fields = ("year_month", "description", "calendar_photo")  # 상세 페이지에서 보여줄 필드
