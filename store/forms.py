from django import forms

from .models import Review


class ReviewForm(forms.models.ModelForm):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
                }),
        )

    class Meta:
        model = Review
        fields = ['rating', 'text','product']
        widgets = {
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
