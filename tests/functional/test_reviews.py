from selenium.webdriver.common.by import By

from .base import FunctionalTest

from store.tests.factories import *


class ReviewTest(FunctionalTest):

    def setUp(self):
        super(ReviewTest, self).setUp()
        # Create a sample product
        self.product = ProductFactory.create()

    def test_name_field_value_is_blank(self):
        # Beverly navigates to the Product Page
        self.browser.get(self.live_server_url +
                         self.product.get_absolute_url())

        # Activate the Reviews tab
        self.browser.find_element(By.LINK_TEXT, 'Reviews').click()

        # She should not see a pre-defined value for the review form name field
        name_field = self.browser.find_element(By.ID, 'id_name')
        self.assertEqual(name_field.get_attribute("placeholder"), "Your Name")
        self.assertEqual(name_field.get_attribute("value"), "")

    def test_cannot_add_empty_reviews(self):
        # Beverly navigates to the Product Page
        self.browser.get(self.live_server_url +
                         self.product.get_absolute_url())

        # Activate the Reviews tab
        self.browser.find_element(By.LINK_TEXT, 'Reviews').click()

        # She accidentally tries to submit an empty review.
        # She hits Enter on the empty input box
        self.browser.find_element(By.ID, 'id_name').send_keys('\n')

        # The page refreshes, and there is an error message saying
        # that the review text cannot be empty
        form = self.browser.find_element(By.ID, 'review-form')
        errors = form.find_elements(By.CSS_SELECTOR, '.has-error')

        # All fields should have an error class
        self.assertEqual(len(errors), 3, "All form fields should raise errors")
        self.assertIn("Please fill in the review", [e.text for e in errors])

    def test_must_fill_all_fields(self):
        # Beverly navigates to the Product Page
        self.browser.get(self.live_server_url +
                         self.product.get_absolute_url())

        # Activate the Reviews tab
        self.browser.find_element(By.LINK_TEXT, 'Reviews').click()

        # She tries again with a valid rating but no review or name
        # Fill in the star rating via jQuery
        form = self.browser.find_element(By.ID, 'review-form')
        self.browser.execute_script("$('#id-rating').rating('update', 3)")
        form.submit()

        # She gets an error message telling her to fill in the empty fields
        errors = form.find_elements(By.CSS_SELECTOR, '.has-error')
        self.assertEqual(
            len(errors), 2, "All Empty fields should raise errors")
        self.assertIn("Please fill in the review", [e.text for e in errors])

        # She tries filling in her name and rating but no review
        self.browser.execute_script("$('#id-rating').rating('update', 3)")
        self.browser.find_element(By.ID, 'id_name').send_keys('Beverly')
        self.browser.find_element(By.ID, 'id_name').submit()

        # She gets an error informing her to fill in the review
        error = form.find_element(By.CSS_SELECTOR, '.has-error')
        self.assertIn("Please fill in the review", error.text)

        # She tries again, filling in all fields, which now works
        self.browser.execute_script("$('#id-rating').rating('update', 3)")
        self.browser.find_element(By.ID, 'id_name').send_keys('Beverly')
        self.browser.find_element(By.ID, 'id_text').send_keys('Good Product')

        self.browser.find_element(By.ID, 'id_name').submit()

        # Assert that the form is no longer visible
        self.wait_for_element_with_id_invisible('review-form')

        # Assert that the success message is displayed
        review_area = self.browser.find_element(By.ID, 'review-area')
        self.assertEqual(
            "Thanks. Your Review has been Posted.", review_area.text)
