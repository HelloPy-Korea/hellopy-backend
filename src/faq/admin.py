<<<<<<< HEAD
from django.contrib import admin

from .models import FAQ

=======
>>>>>>> f62f116 (Style: pre-commit 적용)
# Register your models here.


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")
