from django.contrib import admin

from .models import Notice, NoticeTag, NoticeTagRelation


class NoticeTagRelationInline(admin.TabularInline):
    """Notice에 연결된 태그를 추가하는 인라인"""

    model = NoticeTagRelation
    extra = 1
    autocomplete_fields = ["tag"]  # 태그 자동 완성 기능 추가
    verbose_name = "공지 태그"
    verbose_name_plural = "공지 태그"


@admin.register(NoticeTag)
class ActivityTagAdmin(admin.ModelAdmin):
    """활동 태그 관리자 페이지"""

    list_display = ("id", "name")
    search_fields = ("name",)


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
    inlines = [NoticeTagRelationInline]
