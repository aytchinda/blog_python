# blog/forms/ContactForm.py

from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    # CIVILITY_CHOICES = (
    #      ('Mr', 'Mr'), 
    #     ('Monsieur', 'Monsieur'),
    #     ('Mme', 'Mme'),
    #     ('Madame', 'Madame'),
    #     ('Mlle', 'Mlle'), 
    #     ('Mademoiselle', 'Mademoiselle'),
    # )
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'category', 'is_published', 'tags', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
            'author': forms.Select(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input', 'rows': 5, 'style': 'max-width: 95%;'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'max-width: 95%;'}),
        }
