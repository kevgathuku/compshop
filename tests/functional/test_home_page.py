from .base import FunctionalTest


class HomePageTest(FunctionalTest):

    def test_home_page_loads_successfully(self):
        self.browser.get(self.live_server_url)

        self.assertIn("Home", self.browser.title)


    def test_navbar_links(self):
        self.browser.get(self.live_server_url)

        self.browser.set_window_size(1024, 768)

        homepage_link = self.browser.find_element_by_link_text('HOME')

        homepage_link.click()
        # Assert that the Homepage link works
        self.assertIn("Home", self.browser.title)

        catalogue_link = self.browser.find_element_by_link_text('CATALOGUE')

        catalogue_link.click()
        # Assert that the catalogue link works
        self.assertIn("Catalogue", self.browser.title)
