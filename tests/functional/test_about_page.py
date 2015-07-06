from .base import FunctionalTest


class AboutPageTest(FunctionalTest):

    def test_about_page_navigation(self):
        self.browser.get(self.live_server_url)

        self.browser.set_window_size(1024, 768)

        about_link = self.browser.find_element_by_link_text('ABOUT US')

        about_link.click()

        # Assert that the About Us link in the navbar works
        self.assertIn("About Us", self.browser.title)

        self.assertEqual(self.browser.find_element_by_tag_name('h1').text, 'About Us')
