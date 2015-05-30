from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from .factories import *


class ProductListTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = resolve('/')

        self.assertEqual(response.view_name, 'home')

    def test_home_page_request_uses_correct_template(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')

    def test_correct_context_is_passed_to_template(self):
        featured = ProductFactory.create(featured=True)
        unfeatured = ProductFactory.create(featured=False)

        response = self.client.get(reverse('home'))

        self.assertIn(featured, response.context['featured'])

        self.assertContains(response, featured.name)
        self.assertNotContains(response, unfeatured.name)
