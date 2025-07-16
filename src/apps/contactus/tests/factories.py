import factory
from apps.contactus.models import ContactUs
from apps.contactus.enums import ContactUsEnum


class ContactUsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactUs

    full_name = factory.Faker('name')
    email = factory.LazyAttribute(lambda o: f"user{o.phone_number[-4:]}@example.com")
    phone_number = factory.Sequence(lambda n: f"0912000{n:04d}")
    subject = factory.Iterator(ContactUsEnum)
    message = factory.Faker('paragraph')
