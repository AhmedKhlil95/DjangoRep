from django import forms
from django.contrib.auth.models import User
from accounts.models import UserprofileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserprofileInfo
        fields = ("portfolio", "profile_pic")
        widgets = {
            'portfolio': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Portfolio URL'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
