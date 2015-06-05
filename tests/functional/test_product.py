from .base import FunctionalTest

from store.tests.factories import *


class ProductTest(FunctionalTest):

    def test_product_navigation(self):
        # Create a product
        product = ProductFactory.create()

        # Get the product detail page
        self.browser.get(self.live_server_url + product.get_absolute_url())

        # Assert that the title is as expected
        self.assertIn(product.name, self.browser.title)


    def test_product_navigation_from_homepage(self):
        # Create a sample product
        product1 = ProductFactory.create()

        # Get the homepage
        self.browser.get(self.live_server_url)

        # Navigate to the Product Page
        self.browser.find_element_by_link_text(product1.name).click()

        # Assert that the page is the one expected
        self.assertIn(product1.name, self.browser.title)
