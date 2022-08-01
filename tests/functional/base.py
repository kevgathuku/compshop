from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):

        # Options class instance allows configuring Headless Chrome
        options = Options()
        options.headless = True
        self.browser = webdriver.Chrome(options=options)
        # Wait up to 5 seconds for an element to appear
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    # Explicit wait for an element not to be visible
    def wait_for_element_with_id_invisible(self, element_id):
        WebDriverWait(self.browser, timeout=10).until(
            EC.invisibility_of_element_located((By.ID, element_id))
        )
