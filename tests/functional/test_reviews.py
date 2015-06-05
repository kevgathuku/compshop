from selenium.webdriver.support import expected_conditions as EC

from .base import FunctionalTest

from store.tests.factories import *


class ReviewTest(FunctionalTest):

    def test_cannot_add_empty_reviews(self):
        # Create a sample product
        product = ProductFactory.create()

        # Beverly navigates to the Product Page
        self.browser.get(self.live_server_url + product.get_absolute_url())

        # Activate the Reviews tab
        self.browser.find_element_by_link_text('Reviews').click()

        # She accidentally tries to submit an empty review.
        # She hits Enter on the empty input box
        self.browser.find_element_by_id('id_name').send_keys('\n')

        # The page refreshes, and there is an error message saying
        # that the review text cannot be empty
        errors = self.browser.find_elements_by_css_selector('.has-error')

        # The rating and text fields should have errors
        self.assertIn("Please leave a rating", errors)
        self.assertIn("Please fill in this field", errors)

        # She tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second blank review

        # She receives a similar warning on the product page

        # And she can correct it
