from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    description = models.CharField(_("Descrição"), max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return self.description


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
    show = models.BooleanField(_("Mostrar"), default=True)
    picture = models.ImageField(_("Foto"), blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"