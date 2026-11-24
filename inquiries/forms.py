from django import forms

from inquiries.models import WeddingInquiry


class WeddingInquiryForm(forms.ModelForm):
    class Meta:
        model = WeddingInquiry
        fields = [
            'bride_name',
            'groom_name',
            'wedding_date',
            'location',
            'guest_count',
            'message'
        ]

        widgets = {
            'wedding_date': forms.DateInput(attrs={'type': 'date'})
        }
        help_texts = {
            'guest_count': 'Minimum 60 guests.'
        }