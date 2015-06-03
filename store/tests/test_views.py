from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from store.views import CategoryDetail, ProductDetail, product_review
from .factories import *


class CategoryTest(TestCase):
    """Basic Category Tests"""

    def test_category_absolute_url(self):
        cat1 = CategoryFactory.create()

        self.assertEqual(
            cat1.get_absolute_url(),
            '/category/{}/'.format(cat1.slug,))

    def test_category_url_resolves_to_correct_view(self):
        cat1 = CategoryFactory.create()

        response = resolve(reverse('category', kwargs={'slug': cat1.slug}))

        self.assertEqual(
            response.func.__name__,
            CategoryDetail.as_view().__name__)


class CategoryDisplayTest(TestCase):
    """Test for the CategoryDetail view"""

    def test_category_view_request_uses_correct_template(self):
        cat = CategoryFactory.create()

        response = self.client.get(
            reverse('category', kwargs={'slug': cat.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/category_detail.html')

    def test_correct_context_is_passed_to_category_template(self):
        laptops = CategoryFactory.create()
        other = CategoryFactory.create()

        comp1 = ProductFactory.create(category=laptops)
        other_product = ProductFactory.create(category=other)

        response = self.client.get(
            reverse('category', kwargs={'slug': laptops.slug}))

        # Assert that the Category name is displayed
        self.assertContains(response, laptops.name)
        self.assertNotContains(response, other.name)

        # Products in that category are displayed
        self.assertContains(response, comp1.name)
        self.assertNotContains(response, other_product.name)


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

        # Only featured items should be displayed
        self.assertContains(response, featured.name)
        self.assertNotContains(response, unfeatured.name)


class ProductDetailTest(TestCase):
    """Test for Individual Product Detail View"""

    def test_product_absolute_url(self):
        prod = ProductFactory.create()

        self.assertEqual(
            prod.get_absolute_url(),
            '/products/{}/'.format(prod.slug,))

    def test_product_url_resolves_to_correct_view(self):
        lenovo = ProductFactory.create(name='Lenovo')

        # Returns ResolverMatch object
        response = resolve(lenovo.get_absolute_url())

        self.assertEqual(
            response.func.__name__,
            ProductDetail.as_view().__name__)

    def test_uses_product_detail_template(self):
        product = ProductFactory.create()

        response = self.client.get(product.get_absolute_url())

        self.assertTemplateUsed(response, 'store/product_detail.html')

    def test_product_reviews_are_rendered(self):
        product = ProductFactory.create()
        review = ReviewFactory.create(product=product)

        response = self.client.get(product.get_absolute_url())

        self.assertContains(response, review.name)
        self.assertContains(response, review.text)

    def test_related_products_are_populated_correctly(self):
        products = []

        bulk_cat = CategoryFactory.create()
        products.extend(ProductFactory.create_batch(5, category=bulk_cat))

        response = self.client.get(products[0].get_absolute_url())

        self.assertNotIn(products[0], response.context['related'])
        self.assertEqual(
            len(response.context['related']),
            3,
            "Only 3 related products should be passed in the context")
        for item in response.context['related']:
            self.assertIn(item, products)

    def test_related_products_are_displayed(self):
        products = []

        bulk_cat = CategoryFactory.create()
        products.extend(ProductFactory.create_batch(4, category=bulk_cat))

        response = self.client.get(products[0].get_absolute_url())

        for item in products:
            self.assertContains(response, item.name)


class ProductReviewTest(TestCase):
    """Test for Individual Product Reviews"""

    # TODO: Fix test: Actually resolves to the ProductDetail view
    # def test_product_review_url_resolves_to_correct_view(self):
    #     response = resolve(reverse('products:review'))
    #     self.assertEqual(response.func, product_review)

    def test_product_review_url_handles_POST_requests_only(self):
        response = self.client.get(reverse('products:review'))

        self.assertEqual(response.status_code, 404)
