from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """태그 관리자 페이지"""

    list_display = ("id", "name")
    search_fields = ("name",)
