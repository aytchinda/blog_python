# blog/forms/ContactForm.py

from django import forms
from blog.models import Contact

class ContactForm(forms.ModelForm):
    CIVILITY_CHOICES = (
        ('Mr', 'Mr'),
        ('Mme', 'Mme'),
        ('Mlle', 'Mlle'),
    )

    class Meta:
        model = Contact
        fields = ('civility', 'name', 'email', 'subject', 'message', 'file')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'style': 'max-width: 95%;'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
        }
