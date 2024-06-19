from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser

class CreateUserForm(UserCreationForm):
    terms_checkbox = forms.BooleanField(label='I accept the privacy policy and terms', required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'terms_checkbox']