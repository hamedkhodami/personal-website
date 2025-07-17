from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_contact_email(full_name, email, subject, message):
    subject_line = f"📩 New Contact Message: {subject}"
    body = f"""
You received a new message via contact form:

Full Name: {full_name}
Email: {email}
Subject: {subject}
Message:
{message}
    """

    send_mail(
        subject_line,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
