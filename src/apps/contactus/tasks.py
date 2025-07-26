from django.conf import settings
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_contact_email(full_name, email, subject, message):
    subject_line = f"📩 New Contact Message: {subject}"
    body = (
        f"You received a new message via contact form:\n\n"
        f"Full Name: {full_name}\n"
        f"Email: {email}\n"
        f"Subject: {subject}\n"
        f"Message:\n{message}"
    )

    send_mail(
        subject_line,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )