import pytest
from django.core.exceptions import ValidationError

from core.users.validators import ComplexPasswordValidator


class TestCustomPasswordValidator:
    def test_fails_on_no_uppercase(self):
        password = "testing1234!@#$"
        validator = ComplexPasswordValidator()
        with pytest.raises(ValidationError):
            validator.validate(password)

    def test_fails_on_no_lowercase(self):
        password = "TESTING1234!@#$"
        validator = ComplexPasswordValidator()
        with pytest.raises(ValidationError):
            validator.validate(password)

    def test_fails_on_no_digits(self):
        password = "Testing!@#$"
        validator = ComplexPasswordValidator()
        with pytest.raises(ValidationError):
            validator.validate(password)

    def test_fails_on_no_symbols(self):
        password = "Testing12341234"
        validator = ComplexPasswordValidator()
        with pytest.raises(ValidationError):
            validator.validate(password)
