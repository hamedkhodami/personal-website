from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class ContactUsEnum(TextChoices):
    JOB = 'job', _('Job / Collaboration')
    TECH = 'tech', _('Technical Question')
    OTHER = 'other', _('Other')
