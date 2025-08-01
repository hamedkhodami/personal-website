from django.views.generic import FormView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy

from apps.core.utils import validate_form
from .forms import ContactUsForm
from .tasks import send_contact_email


class ContactUsView(FormView):
    template_name = 'contact/contactus.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contact:thank-you')

    def form_valid(self, form):
        instance = form.save()

        send_contact_email(
            instance.full_name,
            instance.email,
            instance.get_subject_display(),
            instance.message
        )

        messages.success(self.request, _('Your message has been sent successfully.'))
        return super().form_valid(form)

    def form_invalid(self, form):
        validate_form(self.request, form)
        return super().form_invalid(form)



