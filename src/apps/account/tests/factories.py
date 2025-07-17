import factory
from django.utils.crypto import get_random_string
from django.utils import timezone
from apps.account.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    phone_number = factory.Sequence(lambda n: f"0912000{n:04d}")
    email = factory.LazyAttribute(lambda o: f"user{o.phone_number[-4:]}@example.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_active = True
    is_admin = False
    is_verified = False
    token = factory.LazyFunction(lambda: get_random_string(64))
    created_at = factory.LazyFunction(timezone.now)
    updated_at = factory.LazyFunction(timezone.now)
    password = factory.PostGenerationMethodCall("set_password", "123456")
