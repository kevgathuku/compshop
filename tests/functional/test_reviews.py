from selenium.common.exceptions import NoSuchElementException

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
        form = self.browser.find_element_by_id('review-form')
        error = form.find_element_by_css_selector('.has-error')

        # The rating fields should display an error
        self.assertIn("Please leave a valid rating", error.text)

        # She tries again with a valid rating but no review
        # Fill in the star rating via jQuery
        self.browser.execute_script("$('#id-rating').rating('update', 3)")
        form.submit()

        # She gets an error message telling her to fill in her name
        error = form.find_element_by_css_selector('.has-error')
        self.assertEqual("Please fill in your name", error.text)

        # She tries filling in her name and rating but no review
        self.browser.execute_script("$('#id-rating').rating('update', 3)")
        self.browser.find_element_by_id('id_name').send_keys('Beverly')
        self.browser.find_element_by_id('id_name').submit()

        # She gets an error informing her to fill in the review
        error = form.find_element_by_css_selector('.has-error')
        self.assertIn("Please fill in the review", error.text)

        # She tries again, filling in all fields, which now works
        self.browser.execute_script("$('#id-rating').rating('update', 3)")
        self.browser.find_element_by_id('id_name').send_keys('Beverly')
        self.browser.find_element_by_id('id_text').send_keys('Good Product')

        self.browser.find_element_by_id('id_name').submit()

        # Assert that the form has been replaced with a success message
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_id('review-form')

        review_area = self.browser.find_element_by_id('review-area')
        self.assertEqual("Thanks. Your Review has been Posted.", review_area.text)
