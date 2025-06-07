# core/users/validators.py
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class ComplexPasswordValidator:
    def validate(self, password: str, user=None):
        if len(password) < 12:
            raise ValidationError(_("Password must be at least 12 characters long."))

        if not re.search(r"[A-Z]", password):
            raise ValidationError(
                _("Password must contain at least one uppercase letter."),
                code="password_has_no_uppercase",
            )

        if not re.search(r"[a-z]", password):
            raise ValidationError(
                _("Password must contain at least one lowercase letter."),
                code="password_has_no_lowercase",
            )

        if not re.search(r"\d", password):
            raise ValidationError(
                _("Password must contain at least one digit."),
                code="password_has_no_digits",
            )

        if not re.search(r"\W", password):
            raise ValidationError(
                _("Password must contain at least one symbol."),
                code="password_has_no_symbols",
            )

    def get_error_message(self):
        return _("This password is not complex enough.")

    def get_help_text(self):
        return _(
            "Your password must be at least 12 characters long and include "
            "an uppercase letter, a lowercase letter, a number, and a symbol."
        )
