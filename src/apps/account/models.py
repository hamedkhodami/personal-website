from datetime import timedelta
from secrets import token_hex

from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    phone_number = models.CharField(_('Phone number'), max_length=11, unique=True)
    email = models.EmailField(_('Email'), max_length=225, null=True, blank=True)
    first_name = models.CharField(_('First name'), max_length=128, null=True, blank=True)
    last_name = models.CharField(_('Last name'), max_length=128, null=True, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_admin = models.BooleanField(_('Admin'), default=False)
    is_verified = models.BooleanField(_('Verify'), default=False)
    token = models.CharField(_("Secret token"), max_length=64, null=True, blank=True, editable=False)
    created_at = models.DateTimeField(_('Creation time'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update time'), auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.phone_number

    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip() or _('No Name')

    def generate_token(self, byte_size=32):
        self.token = token_hex(byte_size)
        self.save(update_fields=['token'])
        return self.token

    def check_token(self, token):
        return self.token == token

    def last_login_within(self, days):
        if self.last_login:
            local_time = timezone.localtime(self.last_login)
            return local_time >= timezone.now() - timedelta(days=days)
        return False

    @property
    def is_staff(self):
        return self.is_admin
