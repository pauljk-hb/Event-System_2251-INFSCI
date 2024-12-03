from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Custom registration form based on UserCreationForm
# Includes additional fields like email and is_event_manager
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_event_manager']
        widgets = {
            'is_event_manager': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }