from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib import admin

from .models import User
from .forms import UserCreationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = ('id', '__str__', 'first_name', 'last_name', 'is_active', 'is_verified')
    list_display_links = ('id', '__str__',)
    readonly_fields = ('created_at', 'last_login',)
    list_filter = ('is_active', 'is_admin', 'is_verified')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password',)}),
        (_('Personal info'), {'fields': ('email', 'first_name', 'last_name',)}),
        (_('Verifications'), {'fields': ('is_active', 'is_verified', 'is_admin', 'is_superuser')}),
        (_('Dates'), {'fields': ('last_login', 'created_at',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'password1', 'password2'),
        }),
    )

    search_fields = ('phone_number', 'last_name')
    ordering = ('phone_number',)
    date_hierarchy = 'created_at'

