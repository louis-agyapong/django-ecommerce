from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Inventory category table implemented with MPTT
    """

    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(
        _("Slug"), max_length=255, help_text=_("A URL-friendly title."), unique=True, allow_unicode=True
    )
    is_active = models.BooleanField(_("Is active"), default=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("Parent"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product Category")
        verbose_name_plural = _("product categories")
        ordering = ["name"]

    def __str__(self):
        return self.name
