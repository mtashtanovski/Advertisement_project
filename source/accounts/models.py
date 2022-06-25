from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    phone_umber_Regex = RegexValidator(
        regex=r"^\+?996?\d{8,15}$"
    )
    phone_number = models.CharField(
        validators=[phone_umber_Regex],
        max_length=16,
        unique=True
    )
