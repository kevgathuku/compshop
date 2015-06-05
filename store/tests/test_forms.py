from django.test import TestCase

from store.forms import ReviewForm
from .factories import *


class ReviewFormTest(TestCase):

    def test_form_validation_for_blank_items(self):
        p1 = ProductFactory.create()

        form = ReviewForm(
            data={'name':'Kevin', 'text': '', 'product':p1.id})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],["Please fill in the review"])
        self.assertEqual(form.errors['rating'],["Please leave a rating"])

