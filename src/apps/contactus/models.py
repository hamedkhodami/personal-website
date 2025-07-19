from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from .enums import ContactUsEnum


class ContactUs(BaseModel):

    SubjectChoices = ContactUsEnum

    full_name = models.CharField(_('Full name'), max_length=128)
    email = models.EmailField(_('Email'))
    phone_number = models.CharField(_('Phone number'), max_length=15, null=True, blank=True)
    subject = models.CharField(_('Subject'), max_length=32, choices=SubjectChoices.choices,
                               default=SubjectChoices.OTHER)
    message = models.TextField(_('Message'))

    is_read = models.BooleanField(_('Is read?'), default=False)
    is_replied = models.BooleanField(_('Is replied?'), default=False)

    class Meta:
        verbose_name = _('Contactus')
        verbose_name_plural = _('Contactus')

    def __str__(self):
        return f"{self.full_name} - {self.get_subject_display()}"
