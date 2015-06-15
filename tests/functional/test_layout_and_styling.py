import os

from .base import FunctionalTest


class LayoutStylingTest(FunctionalTest):

    def test_bootstrap_links_loaded_successfully(self):
        self.browser.get(self.live_server_url)

        self.assertIn(
            "//netdna.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css",
            self.browser.page_source.strip())

        self.assertIn(
            "//netdna.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js",
            self.browser.page_source.strip())

        self.assertIn(
            '//code.jquery.com/jquery.min.js',
            self.browser.page_source.strip())
