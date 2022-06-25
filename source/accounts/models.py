from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name="profile",
        verbose_name="Профиль",
        on_delete=models.CASCADE,
    )
    phone_umber_Regex = RegexValidator(
        regex=r"^\+?996?\d{8,15}$"
    )
    phone_number = models.CharField(
        validators=[phone_umber_Regex],
        max_length=16, unique=True
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.user.username + "'s Profile"
