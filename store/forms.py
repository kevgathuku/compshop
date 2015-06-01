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
        fields = ['title', 'rating', 'text']
        widgets = {
            'title': forms.fields.TextInput(
                attrs={
                    'placeholder': 'Short Summary e.g. Awesome Product',
                    'class': 'form-control',
                    }),
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Your Review',
                    'class': 'form-control',
                    'rows': 5,
                    }),
        }
