from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name', 'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'id': 'email', 'placeholder': 'Your email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'message', 'placeholder': 'Your message', 'rows': 4
            }),
        }
