from django.contrib import admin
from django.utils.html import format_html

from public.models import ActivityTag, Tag

from .models import ActionPhoto, ActivityAction


class ActivityTagInline(admin.TabularInline):
    """ActivityAction에 연결된 태그를 추가하는 인라인"""

    model = ActivityTag
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "tag":
            # Activity 도메인용 태그만 필터링
            kwargs["queryset"] = Tag.objects.filter(domain="activity")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # 저장 전에 domain 자동 세팅
    def save_new_instance(self, obj, *args, **kwargs):
        if obj.tag and obj.tag.domain != "activity":
            obj.tag.domain = "activity"
            obj.tag.save()

    verbose_name = "활동 태그"
    verbose_name_plural = "활동 태그"


class ActionPhotoInline(admin.TabularInline):
    """ActivityAction에 연결된 사진을 추가하는 인라인"""

    model = ActionPhoto
    extra = 1
    fields = ("image", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        """업로드된 이미지를 미리보기로 표시"""
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover;"/>', obj.image.url
            )
        return "-"


@admin.register(ActivityAction)
class ActivityActionAdmin(admin.ModelAdmin):
    """커뮤니티 활동 관리자 페이지"""

    list_display = ("id", "title", "content_preview")
    search_fields = ("title", "content")
    inlines = [ActivityTagInline, ActionPhotoInline]  # 태그 & 사진 추가 가능

    def content_preview(self, obj):
        """내용이 길 경우 일부만 미리보기"""
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

    content_preview.short_description = "내용 미리보기"
