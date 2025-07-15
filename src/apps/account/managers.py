from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .utils import check_phone_number


class UserManager(BaseUserManager):
    def create_user(self, password=None, phone_number=None):

        if not check_phone_number(phone_number):
            raise ValidationError(_('Entered phone number is not valid'))
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):

        if not phone_number:
            raise ValueError(_('Users must have a mobile number!'))

        user = self.create_user(password, phone_number)

        user.is_admin = True
        user.is_superuser = True
        user.is_verified = True

        user.save(using=self._db)

        return user
