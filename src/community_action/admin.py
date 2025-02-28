from django.contrib import admin
from django.utils.html import format_html

from .models import ActionPhoto, CommunityAction, CommunityTag, Tag


class CommunityTagInline(admin.TabularInline):
    """CommunityAction에 연결된 태그를 추가하는 인라인"""

    model = CommunityTag
    extra = 1
    autocomplete_fields = ["tag"]  # 태그 자동 완성 기능 추가


class ActionPhotoInline(admin.TabularInline):
    """CommunityAction에 연결된 사진을 추가하는 인라인"""

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


@admin.register(CommunityAction)
class CommunityActionAdmin(admin.ModelAdmin):
    """커뮤니티 활동 관리자 페이지"""

    list_display = ("id", "title", "content_preview")
    search_fields = ("title", "content")
    inlines = [CommunityTagInline, ActionPhotoInline]  # 태그 & 사진 추가 가능

    def content_preview(self, obj):
        """내용이 길 경우 일부만 미리보기"""
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

    content_preview.short_description = "내용 미리보기"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """태그 관리자 페이지"""

    list_display = ("id", "name")
    search_fields = ("name",)
