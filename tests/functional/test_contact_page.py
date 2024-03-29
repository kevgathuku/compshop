from selenium.webdriver.common.by import By

from .base import FunctionalTest


class ContactPageTest(FunctionalTest):

    def test_contact_page_navigation(self):
        self.browser.get(self.live_server_url)

        self.browser.set_window_size(1024, 768)

        contact_link = self.browser.find_element(By.LINK_TEXT, 'CONTACT US')

        contact_link.click()

        # Assert that the Contact Us link in the navbar works
        self.assertIn("Contact Us", self.browser.title)

        self.assertEqual(
            self.browser.find_element(By.TAG_NAME, 'h1').text, 'Contact Us'
        )
