from django.contrib import admin

from .models import FAQ

# Register your models here.


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")
