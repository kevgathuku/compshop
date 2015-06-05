"""
Tests for Custom context processors.
"""
import os

from django.conf import settings
from django.test import TestCase, override_settings


class FooterCategoriesContextProcessorTests(TestCase):
    """
    Tests for the ``store.context_processors.footer_categories`` processor.
    """

    def test_custom_context_exists(self):
        # Get the homepage
        response = self.client.get('/')
        self.assertIn('all_categories', response.context)

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
        self.assertNotIn('all_categories', response.context)
