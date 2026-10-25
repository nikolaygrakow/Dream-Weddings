from django.contrib import admin
from django.utils.html import format_html
from weddings.models import Wedding, Review


@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image_preview']
    search_fields = ['name']
    filter_horizontal = ['services']
    ordering = ['id']

    @admin.display(description='Preview')
    def image_preview(self, obj):
        if obj.image:
            image_src = obj.image.url
        elif obj.image_url:
            image_src = obj.image_url
        else:
            return 'No image'

        return format_html(
            '<img src="{}" width="100" height="60" style="object-fit: cover;">',
            image_src
        )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'rating', 'wedding', 'created_at']
    search_fields = ['author_name', 'wedding__name']
    list_filter = ['rating', 'created_at']
    ordering = ['-created_at']