from django.contrib import admin

from .models import Merchandise

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
