"""
    Unit Test file for views
"""
from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pydjango_ci_integration.settings import SITE_URL


class TaskListViewTest(TestCase):
    """
    Test View class
    """
    databases = {'default'}

    def setUp(self):
        # Set up Chrome browser with webdriver-manager
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        # Ensure browser closes after each test
        self.browser.quit()

    def test_chrome_site_homepage(self):
        """
        Test if the Chrome browser can load the homepage
        """
        self.browser.get(SITE_URL)
        self.assertIn('Semaphore', self.browser.title)
