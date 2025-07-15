from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django import forms
from persian_tools import digits
from .utils import check_phone_number
from .models import User


class UserCreationForm(forms.ModelForm):

    phone_number = forms.CharField(label=_('Phone number'), max_length=11)
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password repeat'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number = digits.convert_to_en(phone_number)

        if not check_phone_number(phone_number):
            raise ValidationError(_('Enter a valid phone number'))

        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Passwords are not match.'))

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()

        return user
