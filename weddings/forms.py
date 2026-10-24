from django import forms

from services.models import Service
from weddings.models import Wedding, Review


class WeddingBaseForm(forms.ModelForm):
    class Meta:
        model = Wedding
        fields = '__all__'


class WeddingCreateForm(WeddingBaseForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

class WeddingEditForm(WeddingBaseForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

class WeddingDeleteForm(WeddingBaseForm):
    class Meta(WeddingBaseForm.Meta):
        fields = None
        exclude = ['services', 'image_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'rating', 'comment']



