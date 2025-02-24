from django.contrib import admin
from .models import Md
# Register your models here.

@admin.register(Md)
class MdAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'image')