from .base import FunctionalTest

from store.tests.factories import *


class ProductTest(FunctionalTest):

    def setUp(self):
        super(ProductTest, self).setUp()
        # Create a product
        self.product = ProductFactory.create()

    def test_product_navigation(self):
        # Get the product detail page
        self.browser.get(self.live_server_url + self.product.get_absolute_url())

        # Assert that the title is as expected
        self.assertIn(self.product.name, self.browser.title)


    def test_product_navigation_from_homepage(self):
        # Get the homepage
        self.browser.get(self.live_server_url)

        # Navigate to the Product Page
        self.browser.find_element_by_link_text(self.product.name).click()

        # Assert that the page is the one expected
        self.assertIn(self.product.name, self.browser.title)
