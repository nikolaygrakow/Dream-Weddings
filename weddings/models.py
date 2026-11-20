from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from weddings.validators import validate_past_wedding_date


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

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
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
        return f'{self.author.email} - {self.rating}/5'

    @property
    def stars(self):
        return "⭐" * self.rating


class RealWedding(models.Model):
    bride_name = models.CharField(
        max_length=50,
    )
    groom_name = models.CharField(
        max_length=50,
    )
    description = models.TextField()
    wedding_date = models.DateField(
        validators=[validate_past_wedding_date,]
    )
    location = models.CharField(
        max_length=50,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    services = models.ManyToManyField(
        to='services.Service',
        related_name='real_weddings',
        blank=True,
    )

    def __str__(self):
        return f"{self.bride_name} & {self.groom_name}"


class GalleryImage(models.Model):
    image = models.ImageField(
        upload_to='gallery_images/',
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )
    real_wedding = models.ForeignKey(
        to='RealWedding',
        on_delete=models.CASCADE,
        related_name='gallery_images',
    )

    def __str__(self):
        return f"{self.image.name} - {self.real_wedding}"