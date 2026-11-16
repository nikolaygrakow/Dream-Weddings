from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import WeddingUser


class WeddingUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        error_messages={
        'required': "This field is required.",
        'max_length': "This field cannot exceed 50 characters."
    })
    last_name = forms.CharField(
        max_length=50,
        required=True,
        error_messages={
        'required': "This field is required.",
        'max_length': "This field cannot exceed 50 characters."
    })

    class Meta:
        model = WeddingUser
        fields = ['email', 'first_name', 'last_name']
        error_messages = {
            'email': {
                'unique': "A user with that email already exists.",
                'required': "This field is required.",
                'invalid': "Please enter a valid email address.",
            },
        }

class WeddingUserEditForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        error_messages={
            'required': "This field is required.",
            'max_length': "This field cannot exceed 50 characters."
        })
    last_name = forms.CharField(
        max_length=50,
        required=True,
        error_messages={
            'required': "This field is required.",
            'max_length': "This field cannot exceed 50 characters."
        })

    class Meta:
        model = WeddingUser
        fields = ['first_name', 'last_name']
