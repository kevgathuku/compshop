from .base import FunctionalTest


class LayoutStylingTest(FunctionalTest):

    def test_bootstrap_links_loaded_successfully(self):
        self.browser.get(self.live_server_url)

        links = [link.get_attribute("href")
                 for link in self.browser.find_elements_by_tag_name('link')]
        scripts = [script.get_attribute("src")
                   for script in self.browser.find_elements_by_tag_name('script')]

        self.assertTrue(
            ["//netdna.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css"
             in link for link in links])

        self.assertTrue(
            ["//netdna.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"
             in link for link in links])

        self.assertTrue(
            ["//code.jquery.com/jquery.min.js"
             in link for link in scripts])
