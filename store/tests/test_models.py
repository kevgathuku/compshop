from django.core.exceptions import ValidationError
from django.test import TestCase

from .factories import ReviewFactory


class ReviewModelTest(TestCase):

    def test_cannot_save_empty_reviews(self):
        with self.assertRaises(ValidationError):
            review = ReviewFactory.create(text='')
            review.full_clean()
