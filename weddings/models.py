from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Wedding(models.Model):
    name = models.CharField(
        max_length=100,
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[
            MinValueValidator(
                Decimal('0.01'),
                message='Price must be greater than zero. Minimum allowed price is €0.01.'),
        ]
    )

    description = models.TextField()
    image_url = models.URLField(
        blank=True,
    )
    image = models.ImageField(
        upload_to='wedding_images/',
        blank=True,
        null=True,
    )

    services = models.ManyToManyField(
        'services.Service',
        related_name='weddings',
        blank=True,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    author_name = models.CharField(
        max_length=50,
    )

    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    wedding = models.ForeignKey(
        'Wedding',
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    def __str__(self):
        return f'{self.author_name} - {self.rating}/5'

    @property
    def stars(self):
        return "⭐" * self.rating
