from django import forms
from services.models import Service
from weddings.models import Wedding, Review


class WeddingBaseForm(forms.ModelForm):
    class Meta:
        model = Wedding
        fields = '__all__'
        help_texts = {
            'image_url': 'Paste an image URL or upload an image below.',
            'image': 'Upload an image or provide an image URL above.',
        }

class WeddingImageValidationForm(WeddingBaseForm):
    def clean(self):
        cleaned_data = super().clean()
        image_url = cleaned_data.get('image_url')
        image = cleaned_data.get('image')

        if not image_url and not image:
            raise forms.ValidationError('Please provide an image URL or upload an image!')

        return cleaned_data

class WeddingCreateForm(WeddingImageValidationForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

class WeddingEditForm(WeddingImageValidationForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

class WeddingDeleteForm(WeddingBaseForm):
    class Meta(WeddingBaseForm.Meta):
        fields = None
        exclude = ['services', 'image_url', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'rating', 'comment']
