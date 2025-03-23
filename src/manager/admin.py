from django.contrib import admin

from .models import Manager

# Register your models here.


@admin.register(Manager)
class ManagementInfoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
        "email",
        "linkedin",
        "github",
        "photo",
    )
    fields = (
        "name",
        "role",
        "email",
        "linkedin",
        "github",
        "photo",
    )

    def delete_model(self, request, obj):
        # Admin에서 개별 객체 삭제 시 호출됨
        obj.delete()

    def delete_queryset(self, request, queryset):
        # Admin에서 여러 객체 삭제 시 호출됨
        for obj in queryset:
            obj.delete()
