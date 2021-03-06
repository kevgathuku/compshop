from django.test import TestCase

from store.forms import ReviewForm
from store.models import Review
from .factories import *


class ReviewFormTest(TestCase):

    def test_form_validation_for_blank_items(self):
        p1 = ProductFactory.create()

        form = ReviewForm(
            data={'name':'', 'text': '', 'product':p1.id})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],["Please fill in the review"])
        self.assertEqual(form.errors['rating'],["Please leave a rating"])

    def test_form_validation_for_invalid_review(self):
        p1 = ProductFactory.create()

        form = ReviewForm(
            data={'name':'', 'text': '', 'rating': 0, 'product':p1.id})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],["Please fill in the review"])
        self.assertEqual(form.errors['rating'],["Please leave a valid rating"])

    def test_form_validation_for_required_name_field(self):
        p1 = ProductFactory.create()

        form = ReviewForm(
            data={'name':'', 'text': 'Hello', 'rating': 2, 'product':p1.id})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'],['Please fill in your name'])

    def test_form_save_handles_saving_product_reviews(self):
        prod = ProductFactory.create()

        form = ReviewForm(
            data={'name':'Kevin', 'text': 'Review', 'rating': 3, 'product':prod.id})

        new_review = form.save()

        self.assertEqual(new_review, Review.objects.first())
        self.assertEqual(new_review.name, 'Kevin')
        self.assertEqual(new_review.product, prod)
