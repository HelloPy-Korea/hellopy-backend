from django.contrib import admin

from .models import Merchandise

# Register your models here.


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "is_visible")
    list_editable = ("is_visible",)
    search_fields = ("name", "description")
    exclude = ("is_deleted",)

    def delete_queryset(self, request, queryset):
        # Admin에서 여러 객체 삭제 시 호출됨
        for obj in queryset:
            obj.delete()
