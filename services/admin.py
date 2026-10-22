from django.contrib import admin

from services.models import Service

# TODO промяна полетата

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'category',
        'phone',
        'description'
    ]
    ordering = ['id']
    search_fields = ['name', 'category']


