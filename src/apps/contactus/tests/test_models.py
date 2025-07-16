import pytest
from apps.contactus.models import ContactUs
from apps.contactus.tests.factories import ContactUsFactory
from apps.contactus.enums import ContactUsEnum


@pytest.mark.django_db
class TestContactUsModel:

    def test_contactus_creation(self):
        contact = ContactUsFactory()
        assert isinstance(contact, ContactUs)
        assert contact.full_name != ""
        assert contact.message != ""
        assert "@" in contact.email

    def test_contactus_str_method(self):
        contact = ContactUsFactory(subject=ContactUsEnum.TECH, full_name="Sara Ahmadi")
        expected_str = f"Sara Ahmadi - {ContactUsEnum.TECH.label}"
        assert str(contact) == expected_str

    def test_default_boolean_fields(self):
        contact = ContactUsFactory()
        assert contact.is_read is False
        assert contact.is_replied is False
