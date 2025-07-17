# apps/contact/forms.py

from django import forms
from django.utils.translation import gettext_lazy as _
from persian_tools import digits
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': _('Your message...')}),
        }

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name', '').strip()
        if len(name) < 3:
            raise forms.ValidationError(_('Full name must be at least 3 characters long.'))
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if not email or '@' not in email:
            raise forms.ValidationError(_('Enter a valid email address.'))
        return email.lower()

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number', '').strip()
        if phone:
            phone = digits.convert_to_en(phone)
            if not phone.isdigit() or not 10 <= len(phone) <= 15:
                raise forms.ValidationError(_('Enter a valid phone number.'))
        return phone

    def clean_message(self):
        msg = self.cleaned_data.get('message', '').strip()
        if len(msg) < 10:
            raise forms.ValidationError(_('Message must be at least 10 characters long.'))
        return msg
