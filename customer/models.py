from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    name = models.CharField(
        max_length=64,
        default="",
        blank=True,
        help_text=_("Customer Name")
    )
    birthdate = models.DateField(
        verbose_name=_("Birthday"),
        help_text=_("Customer Birthdate")
    )
    email = models.EmailField(help_text=_("email address of the customer"))

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"