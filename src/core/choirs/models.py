from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.base.models import BaseModel


class BaseChoir(BaseModel):
    name = models.CharField(_("name"), max_length=80)
    description = models.TextField(_("description"), max_length=250)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("created by"),
    )

    def __str__(self):
        return self.name

    class Meta:  # type: ignore
        abstract = True
