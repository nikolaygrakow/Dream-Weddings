from django.contrib import admin
from inquiries.models import WeddingInquiry


@admin.register(WeddingInquiry)
class WeddingInquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'wedding', 'wedding_date', 'guest_count', 'status', 'created_at']
    list_filter = ['status', 'wedding_date', 'created_at']
    search_fields = ['user__email', 'bride_name', 'groom_name', 'location']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'status']
    list_per_page = 20
