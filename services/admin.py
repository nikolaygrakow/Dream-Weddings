from django.contrib import admin
from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'phone', 'email']
    list_filter = ['category']
    search_fields = ['name', 'category', 'email']
    ordering = ['id']
