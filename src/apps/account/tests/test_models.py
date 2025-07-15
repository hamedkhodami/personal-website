import pytest
from apps.account.models import User
from apps.account.tests.factories import UserFactory


@pytest.mark.django_db
class TestUserModel:

    def test_user_creation(self):
        user = UserFactory()
        assert isinstance(user, User)
        assert user.phone_number.startswith("0912")
        assert user.check_password("123456")
        assert user.is_active is True

    def test_user_full_name(self):
        user = UserFactory(first_name="Ali", last_name="Rezaei")
        assert user.full_name() == "Ali Rezaei"

        user = UserFactory(first_name="", last_name="")
        assert user.full_name() == "بدون نام" or user.full_name() == "No Name"  # بسته به زبان پروژه

    def test_token_generation_and_check(self):
        user = UserFactory(token=None)
        token = user.generate_token()
        assert token == user.token
        assert user.check_token(token) is True
        assert user.check_token("fake_token") is False

    def test_is_staff_property(self):
        admin_user = UserFactory(is_admin=True)
        normal_user = UserFactory(is_admin=False)

        assert admin_user.is_staff is True
        assert normal_user.is_staff is False
