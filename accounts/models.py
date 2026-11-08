from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import WeddingUserManager


class WeddingUser(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
    )

    objects = WeddingUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
