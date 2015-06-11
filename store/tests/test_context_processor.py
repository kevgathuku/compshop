"""
Tests for Custom context processors.
"""
import os

from django.conf import settings
from django.test import TestCase, override_settings


class ProductCategoriesContextProcessorTests(TestCase):
    """
    Tests for the ``store.context_processors.product_categories`` processor.
    """

    def test_custom_context_exists(self):
        # Get the homepage
        response = self.client.get('/')
        self.assertIn('product_categories', response.context)

    @override_settings(
    TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(settings.BASE_DIR, 'templates')],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
    )
    def test_custom_context_does_not_exist_if_not_included_in_settings(self):
        # Get the homepage
        response = self.client.get('/')
        self.assertNotIn('product_categories', response.context)
