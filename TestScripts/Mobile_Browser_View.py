import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Mobile_View(unittest.TestCase):
    def setUp(self):
        opts = Options()
        #Changing Mobile view (By sending respective Window Size)
        opts.add_argument("window-size=375,812")
        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

    def test_mobile_browser(self):
        # Target URL
        self.driver.get("https://www.borrowlenses.com/")

    def tearDown(self):
        # close the browser window
        self.driver.quit()
