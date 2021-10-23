from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("name"), max_length=255, db_index=True)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ("name",)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE, verbose_name=_("category")
    )
    name = models.CharField(_("name"), max_length=255, db_index=True)
    slug = models.SlugField(_("slug"), max_length=255, db_index=True)
    image = models.ImageField(_("image"), upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(_("description"), blank=True)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    available = models.BooleanField(_("available"), default=True)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name
