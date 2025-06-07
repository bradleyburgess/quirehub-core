import uuid

import pytest
from django.db.utils import IntegrityError
from faker import Faker

from core.users.models import User


class TestUserModel:
    fake = Faker()

    def test_user_has_no_username(self):
        email = self.fake.email()
        password = self.fake.password()
        user = User(email=email, password=password)
        assert not hasattr(user, "username")

    def test_user_has_uuid(self):
        email = self.fake.email()
        password = self.fake.password()
        user = User(email=email, password=password)
        assert hasattr(user, "uuid")
        assert isinstance(user.uuid, uuid.UUID)

    @pytest.mark.django_db
    def test_unique_emails(self):
        email = self.fake.email()
        password = self.fake.password()
        User.objects.create_user(email=email, password=password)  # type: ignore
        with pytest.raises(IntegrityError):
            User.objects.create_user(email=email, password=password)  # type: ignore

    @pytest.mark.django_db
    def test_unique_emails_case_insensitive(self):
        email = self.fake.email().lower()
        password = self.fake.password()
        User.objects.create_user(email=email, password=password)  # type: ignore
        with pytest.raises(IntegrityError):
            User.objects.create_user(email=email.upper(), password=password)  # type: ignore
