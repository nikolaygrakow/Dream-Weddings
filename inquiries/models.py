from django.core.validators import MinValueValidator
from django.db import models

from inquiries.validators import validate_wedding_date


class WeddingInquiry(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    bride_name = models.CharField(
        max_length=50,
    )
    groom_name = models.CharField(
        max_length=50,
    )
    wedding_date = models.DateField(
        validators=[validate_wedding_date]
    )
    location = models.CharField(
        max_length=50,
    )
    guest_count = models.PositiveIntegerField(
        validators=[MinValueValidator(60),]
    )
    message = models.TextField(
        blank=True,
    )
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        to='accounts.WeddingUser',
        on_delete=models.CASCADE,
        related_name='inquiries',
    )
    wedding = models.ForeignKey(
        to='weddings.Wedding',
        on_delete=models.PROTECT,
        related_name='inquiries',
    )

    def __str__(self):
        return f"Inquiry for {self.wedding} from {self.user}"