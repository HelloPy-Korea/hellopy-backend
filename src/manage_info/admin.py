from django.contrib import admin
from .models import ManagementInfo

# Register your models here.

@admin.register(ManagementInfo)
class ManagementInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email')