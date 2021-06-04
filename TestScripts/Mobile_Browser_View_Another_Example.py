import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Mobile_View(unittest.TestCase):
    def setUp(self):
        #Changing Mobile view (By sending respective Window Size)
        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_size(375,812)
    def test_mobile_browser(self):
        # Target URL
        self.driver.get("https://www.borrowlenses.com/")

    def tearDown(self):
        # close the browser window
        self.driver.quit()
