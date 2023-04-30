from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    first_name = models.CharField(_("Primeiro Nome"), max_length=50, null=False, blank=False)
    last_name = models.CharField(_("Sobrenome"), max_length=50, null=False, blank=False)
    phone = models.CharField(_("Nº Telefone"), max_length=50, null=False, blank=False, unique=True)
    email = models.EmailField(
        "Email",
        max_length=254,
        blank=True,
    )
    created_date = models.DateTimeField(_("data de entrada"), auto_now_add=True)
    description = models.TextField(_("Descrição"), blank=True)
    # show = models.BooleanField(_("Visualizar"), default=True)
    # category = models.ForeignKey()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"