from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 95%;'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 95%;'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 95%;'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 95%;'})
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
