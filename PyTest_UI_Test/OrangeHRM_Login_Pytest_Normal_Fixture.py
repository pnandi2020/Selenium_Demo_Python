# Import the 'modules' that are required for execution for Selenium test automation
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


# Fixture for Firefox
@pytest.fixture(scope="class")
def firefox_driver_init(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("firefox_driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        title = "Google"
        assert title == self.driver.title

        search_text = "ISTQB"
        search_box = self.driver.find_element_by_xpath("//input[@name='q']")
        search_box.send_keys(search_text)

        time.sleep(5)

        # Option 1 - To Submit the search
        # search_box.submit()

        # Option 2 - To Submit the search
        search_box.send_keys(Keys.ARROW_DOWN)
        search_box.send_keys(Keys.ARROW_UP)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

        # Click on the LambdaTest HomePage Link
        title = "Certifying Software Testers Worldwide - ISTQB® International Software Testing Qualifications Board"
        lt_link = self.driver.find_element_by_xpath(
            "//h3[contains(text(),'Certifying Software Testers Worldwide - ISTQB® Int')]")
        lt_link.click()

        time.sleep(5)
        assert title == self.driver.title
        time.sleep(2)


@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass


class Test_URL_Chrome(Basic_Chrome_Test):
    def test_open_url(self):
        # Step 2) Navigate to OrangeHRM
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        # Step 3) Enter the Username & Enter Password
        username = self.driver.find_element_by_name("txtUsername")
        password = self.driver.find_element_by_name("txtPassword")
        submit = self.driver.find_element_by_name("Submit")
        username.send_keys("Admin")
        password.send_keys("admin123")
        # Step 4) Click Login
        submit.click()

        #Logout from application
        self.driver.find_element_by_id("welcome").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)