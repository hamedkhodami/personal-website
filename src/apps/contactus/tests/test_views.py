import pytest
from django.urls import reverse
from apps.contactus.models import ContactUs
from apps.contactus.enums import ContactUsEnum


@pytest.mark.django_db
class TestContactUsView:

    def test_valid_contactus_submission(self, client):
        data = {
            "full_name": "Ali Rezaei",
            "email": "ali@example.com",
            "phone_number": "09123456789",
            "subject": ContactUsEnum.JOB.value,
            "message": "I’m interested in joining your team!",
        }
        response = client.post(reverse("contact:contact-us"), data)
        assert response.status_code == 302  # Redirect to thank-you
        assert response.url == reverse("contact:thank-you")
        assert ContactUs.objects.filter(email="ali@example.com").exists()

    def test_invalid_contactus_submission(self, client):
        data = {
            "full_name": "Al",
            "email": "no-at-symbol",
            "phone_number": "abc123",
            "subject": "not-valid",
            "message": "Hi",
        }
        response = client.post(reverse("contact:contact-us"), data)
        assert response.status_code == 200
        assert "form" in response.context
        assert response.context["form"].errors
        assert ContactUs.objects.count() == 0
