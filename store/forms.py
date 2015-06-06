from django import forms

from .models import Review


class ReviewForm(forms.models.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'text','product']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
                }),
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Your Review',
                    'class': 'form-control',
                    'rows': 5,
                    }),
            'product': forms.HiddenInput(),
        }
        error_messages = {
            'text': {'required': "Please fill in the review"},
            'rating': {'required': "Please leave a rating"}
            }
