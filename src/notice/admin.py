from django.contrib import admin

from public.models import NoticeTag, Tag

from .models import Notice


class NoticeTagInline(admin.TabularInline):
    model = NoticeTag
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "tag":
            # Notice 도메인용 태그만 필터링
            kwargs["queryset"] = Tag.objects.filter(domain="notice")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # 저장 전에 domain 자동 세팅
    def save_new_instance(self, obj, *args, **kwargs):
        if obj.tag and obj.tag.domain != "notice":
            obj.tag.domain = "notice"
            obj.tag.save()

    verbose_name = "공지 태그"
    verbose_name_plural = "공지 태그"


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_pinned")
    list_filter = ("is_pinned",)
    search_fields = ("title", "content")
    ordering = ("-created_at",)

    fieldsets = (("수정 가능 필드", {"fields": ("title", "content", "is_pinned")}),)
    inlines = [NoticeTagInline]
