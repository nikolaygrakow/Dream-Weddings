from django.db import models

from services.choices import ServiceCategoryChoices


class Service(models.Model):

    name = models.CharField(
        max_length=100,
    )

    category = models.CharField(
        max_length=20,
        choices=ServiceCategoryChoices.choices,
    )

    phone = models.CharField(
        max_length=20,
    )

    description = models.TextField()

    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
