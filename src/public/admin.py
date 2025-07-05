from django.contrib import admin

from .image_models import TemporaryImage
from .tag_models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """태그 관리자 페이지"""

    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(TemporaryImage)
class TemporaryImageAdmin(admin.ModelAdmin):
    """임시 이미지 관리자 페이지"""

    list_display = ("id", "path", "expiry_at")
    search_fields = ("path",)

    def has_add_permission(self, request):
        return False  # 추가 비활성화

    def has_change_permission(self, request, obj=None):
        return False  # 수정 비활성화

    def delete_queryset(self, request, queryset):
        # Admin에서 여러 객체 삭제 시 호출됨
        for obj in queryset:
            obj.delete()
