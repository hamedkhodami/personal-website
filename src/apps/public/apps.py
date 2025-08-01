from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PublicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.public'
    verbose_name = _('Public')
