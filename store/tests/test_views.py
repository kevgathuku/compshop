from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from store.views import ProductDetail
from .factories import *


class ProductListTest(TestCase):
    """Test for the ProductList displayed on Home Page"""

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


class ProductDetailTest(TestCase):
    """Test for Individual Product Detail View"""

    def test_post_url_resolves_to_correct_view(self):
        lenovo = ProductFactory.create(name='Lenovo')

        # Returns ResolverMatch object
        response = resolve(reverse('products:detail', kwargs={'product_id': lenovo.id}))

        self.assertEqual(
            response.func.__name__,
            ProductDetail.as_view().__name__)

    def test_uses_product_detail_template(self):
        product = ProductFactory.create()

        response = self.client.get(reverse('products:detail', args=[product.id]))

        self.assertTemplateUsed(response, 'store/product_detail.html')

    def test_product_reviews_are_rendered(self):
        product = ProductFactory.create()
        review = ReviewFactory.create(product=product)

        response = self.client.get(reverse('products:detail', args=[product.id]))

        self.assertContains(response, review.name)
        self.assertContains(response, review.text)
