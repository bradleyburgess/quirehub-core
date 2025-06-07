import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import SoftDeleteAllManager, SoftDeleteManager


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


class SoftDeleteMixin(models.Model):
    """
    Adds soft deletion. `delete()` sets `deleted_at` to now, and `hard_delete()`
    does a traditional hard deletion, removing the record.
    """

    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteAllManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False) -> tuple[int, dict[str, int]]:
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])
        return 1, {self.__class__.__name__: 1}

    def hard_delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)

    def restore(self):
        self.deleted_at = None
        self.save(update_fields=["deleted_at"])


class BaseModel(TimestampsMixin, UuidMixin):
    """
    The `BaseModel` includes a UUID field for public-facing identification and
    URLS, as well as `created_at` and `modified_at` timestamps
    """

    class Meta:  # type: ignore
        abstract = True
