from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='repeat-password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_confirm_password(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError("Password doesn't match ")
        return cleaned_data['password']
