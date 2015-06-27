from .base import FunctionalTest


class ErrorPagesTest(FunctionalTest):

    def test_404_response(self):
        self.browser.get(self.live_server_url + '/does-not-exist')

        self.assertIn("Page Not Found", self.browser.title)
