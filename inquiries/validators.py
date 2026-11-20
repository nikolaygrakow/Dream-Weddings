from django.utils import timezone

from django.core.exceptions import ValidationError


def validate_wedding_date(date):
    if date <= timezone.localdate():
        raise ValidationError("Wedding date must be later than today's date.")
