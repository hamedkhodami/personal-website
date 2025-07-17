from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'subject', 'is_read', 'is_replied', 'created_at')
    list_display_links = ('id', 'full_name')
    list_filter = ('subject', 'is_read', 'is_replied')
    search_fields = ('full_name', 'email', 'phone_number', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('full_name', 'email', 'phone_number', 'subject', 'message')
        }),
        (_('Status'), {
            'fields': ('is_read', 'is_replied')
        }),
        (_('Metadata'), {
            'fields': ('created_at',)
        }),
    )