from django.core.urlresolvers import resolve, reverse
from django.http import HttpRequest
from django.test import TestCase
from django.views.defaults import server_error

from store.views import (AboutView, CategoryDetail, ContactView, ProductDetail,
                         product_review)
from .factories import *


class AboutViewTest(TestCase):
    """Tests for the About View"""

    def test_about_url_resolves_to_correct_view(self):
        response = resolve(reverse('about'))

        self.assertEqual(
            response.func.__name__,
            AboutView.as_view().__name__)


class ContactViewTest(TestCase):
    """Tests for the Contact View"""

    def test_about_url_resolves_to_correct_view(self):
        response = resolve(reverse('contact'))

        self.assertEqual(
            response.func.__name__,
            ContactView.as_view().__name__)


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

    def test_categories_context(self):
        cat1 = CategoryFactory.create()
        cat2 = CategoryFactory.create()

        product1 = ProductFactory.create(category=cat1)

        response = self.client.get('/')

        # The category without a related product is not in the context
        self.assertIn(cat1, response.context['product_categories'])
        self.assertNotIn(cat2, response.context['product_categories'])

    def test_categories_are_displayed_in_homepage(self):
        cat1 = CategoryFactory.create()
        cat2 = CategoryFactory.create()

        product1 = ProductFactory.create(category=cat1)

        response = self.client.get('/')

        self.assertContains(response, cat1.name)
        self.assertNotContains(response, cat2.name)


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

        response = self.client.get(laptops.get_absolute_url())

        # Assert that the Category name is displayed
        self.assertContains(response, laptops.name)
        # Assert that the correct Category object is in the context
        self.assertEqual(laptops, response.context['object'])

        # Products in that category are displayed
        self.assertContains(response, comp1.name)


class ProductListTest(TestCase):
    """Test for the ProductList displayed on Home Page"""

    def test_root_url_resolves_to_home_page_view(self):
        response = resolve('/')

        self.assertEqual(response.view_name, 'home')

    def test_home_page_request_uses_correct_template(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')

    def test_correct_featured_products_are_passed_to_template(self):
        featured = ProductFactory.create(featured=True)
        unfeatured = ProductFactory.create(featured=False)

        response = self.client.get(reverse('home'))

        self.assertIn(featured, response.context['featured'])
        self.assertNotIn(unfeatured, response.context['featured'])

    def test_latest_products_are_passed_to_template(self):
        prods = ProductFactory.create_batch(10)

        response = self.client.get(reverse('home'))

        # 3 latest products are passed in the context
        self.assertEqual(3, len(response.context['latest']))
        # Test that the 2 lists contain the same products
        self.assertCountEqual(prods[-3:], response.context['latest'])


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

    def test_product_review_url_resolves_to_correct_view(self):
        response = resolve(reverse('products:review'))
        self.assertEqual(response.func, product_review)

    def test_product_review_url_handles_POST_requests_only(self):
        response = self.client.get(reverse('products:review'))

        self.assertEqual(response.status_code, 404)

    def test_correct_response_is_returned_on_successful_post(self):
        product = ProductFactory.create()

        response = self.client.post(
            reverse('products:review'),
            data={'name':'Kevin', 'text': 'Some Text', 'rating': 5, 'product': product.id})

        expected_response = {"reviewRating": "", "reviewName": "", "reviewText": ""}

        self.assertJSONEqual(response.content.decode(), expected_response)

    def test_correct_error_response_is_returned_on_wrong_input(self):
        product = ProductFactory.create()

        response = self.client.post(
            reverse('products:review'),
            data={'name':'', 'text': 'Some Text', 'rating': 5, 'product': product.id})

        expected_response = {"reviewRating": "", "reviewName": 'Please fill in your name', "reviewText": ""}

        self.assertJSONEqual(response.content.decode(), expected_response)

    def test_correct_error_response_is_returned_on_wrong_input_for_two_fields(self):
        product = ProductFactory.create()

        response = self.client.post(
            reverse('products:review'),
            data={'name':'', 'text': '', 'rating': 5, 'product': product.id})

        expected_response = {"reviewRating": "",
                             "reviewName": 'Please fill in your name',
                             "reviewText": "Please fill in the review"}

        self.assertJSONEqual(response.content.decode(), expected_response)

    def test_correct_error_response_is_returned_for_all_invalid_inputs(self):
        product = ProductFactory.create()

        response = self.client.post(
            reverse('products:review'),
            data={'name':'', 'text': '', 'rating': 8, 'product': product.id})

        expected_response = {"reviewRating": "Please leave a valid rating",
                             "reviewName": 'Please fill in your name',
                             "reviewText": "Please fill in the review"}

        self.assertJSONEqual(response.content.decode(), expected_response)


class ErrorTests(TestCase):
    """Test for 50x errors"""

    def test_500_error_response(self):
        request = HttpRequest()
        response = server_error(request)

        self.assertContains(response, 'Ooops!!! 500', status_code=500)
