from django import forms
from services.models import Service



class ServiceBaseForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        error_messages = {
            'email': {
                'unique': 'Service with this Email already exists.',
            }
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits!')

        return phone


class ServiceCreateForm(ServiceBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].required = False
        self.fields['category'].widget = forms.HiddenInput()

class ServiceEditForm(ServiceBaseForm):
    pass


class ServiceDeleteForm(ServiceBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True

