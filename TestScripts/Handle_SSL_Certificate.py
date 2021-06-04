import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Mobile_View(unittest.TestCase):
    def setUp(self):
        opts = Options()
        # Option 1
        '''opts.add_argument('--allow-running-insecure-content')
        opts.add_argument('--ignore-certificate-errors')'''
        #Option 2
        opts.set_capability("acceptInsecureCerts", True)

        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

    def test_mobile_browser(self):
        # Target URL
        self.driver.get("https://expired.badssl.com/")
        #assert self.driver.title() == 'expired.badssl.com'
        self.driver.implicitly_wait(5000)
        titleOfWebPage = self.driver.title
        self.assertEqual('expired.badssl.com',titleOfWebPage,'webpage title is not matching')
    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == "__main__":
	unittest.main()