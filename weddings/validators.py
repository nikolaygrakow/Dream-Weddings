from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_past_wedding_date(date):
    if date >= timezone.localdate():
        raise ValidationError("Wedding date must be earlier than today's date.")