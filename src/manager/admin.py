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
