from django import forms

from .models import Review


class ReviewForm(forms.models.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True

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
            'name': {'required': 'Please fill in your name'},
            'rating': {'required': "Please leave a rating",
                       'invalid_choice': 'Please leave a valid rating'}
            }
