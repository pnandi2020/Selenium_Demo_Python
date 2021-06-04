import unittest
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test(unittest.TestCase):
    def test_open_alerts(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(3000)
        # open webpage
        driver.get("https://netbanking.hdfcbank.com/netbanking/")
        # switch to frame1
        driver.switch_to.frame(0)
        # set the value of the textbar to the value stored
        driver.find_element_by_css_selector("input[class='input_password']").send_keys('1000')
        driver.find_element_by_xpath("//img[@alt='continue']").click()
        driver.switch_to.default_content()
        driver.switch_to.frame(1)
        driver.find_element_by_link_text('Terms and Conditions').click()
        sleep(50)
        page_title = driver.title
        print(page_title)


if __name__ == "__main__":
    unittest.main()
