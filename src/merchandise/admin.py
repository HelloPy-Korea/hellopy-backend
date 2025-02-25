from django.contrib import admin

from .models import Merchandise

# Register your models here.

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'image')