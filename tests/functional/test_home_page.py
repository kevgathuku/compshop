from store.tests.factories import CategoryFactory, ProductFactory
from .base import FunctionalTest


class HomePageTest(FunctionalTest):

    def test_home_page_loads_successfully(self):
        self.browser.get(self.live_server_url)

        self.assertIn("Home", self.browser.title)

    def test_category_sidebar_display(self):
        cat1 = CategoryFactory.create()
        cat2 = CategoryFactory.create()

        product1 = ProductFactory.create(category=cat1)

        self.browser.get(self.live_server_url)

        menu = self.browser.find_element_by_id('main_menu')

        self.assertIn(
            cat1.name,
            menu.text,
            "Categories with products should be visible on the sidebar")
        self.assertNotIn(
            cat2.name,
            menu.text,
            "Categories without products should not be visible on the sidebar")

        def test_category_footer_display(self):
            cat1 = CategoryFactory.create()
            cat2 = CategoryFactory.create()

            product1 = ProductFactory.create(category=cat1)

            self.browser.get(self.live_server_url)

            menu = self.browser.find_element_by_tag_name('footer')

            self.assertIn(
                cat1.name,
                menu.text,
                "Categories with products should be visible in the footer")
            self.assertNotIn(
                cat2.name,
                menu.text,
                "Categories without products should not be visible in the footer")


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
