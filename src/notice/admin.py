from django.contrib import admin

from .models import Notice


# Register your models here.
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_pinned", "created_at", "updated_at")
    list_filter = ("is_pinned",)
    search_fields = ("title", "content")
    ordering = ("-created_at",)

    fieldsets = (
        ("수정 가능 필드", {"fields": ("title", "content", "is_pinned")}),
        ("자동 설정 필드", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    readonly_fields = ("created_at", "updated_at")
