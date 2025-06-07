import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampsMixin(models.Model):
    """
    The `TimestampsMixin` adds `created_at` and `modified_at` timestamps.
    """

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("modified at"), auto_now=True)

    class Meta:
        abstract = True


class UuidMixin(models.Model):
    """
    The `UuidMixin` adds a `uuid` field to the model, which is used for
    public-facing URLS.
    """

    uuid = models.UUIDField(
        _("UUID"), default=uuid.uuid4, editable=False, unique=True, db_index=True
    )

    class Meta:
        abstract = True


class BaseModel(TimestampsMixin, UuidMixin):
    """
    The `BaseModel` includes a UUID field for public-facing identification and
    URLS, as well as `created_at` and `modified_at` timestamps
    """

    class Meta:  # type: ignore
        abstract = True
