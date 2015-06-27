from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()
        # Wait up tp 10 seconds for an element to appear
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    # Explicit wait for an element not to be visible
    def wait_for_element_with_id_invisible(self, element_id):
        WebDriverWait(self.browser, timeout=10).until_not(
                lambda b: b.find_element_by_id(element_id).is_displayed()
            )
