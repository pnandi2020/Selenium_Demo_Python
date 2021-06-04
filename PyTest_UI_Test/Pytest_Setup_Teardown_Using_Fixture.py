from __future__ import print_function
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def resource_a_setup(request):
    print('\nresources_a_setup()')
    # create a new Chrome session
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    # Target URL
    web_driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("resource_a_setup")
class BasicTest:
    pass


class Test_OrangeHRM_Login(BasicTest):
    def test_1_that_needs_resource_a(self):
        print('test_1_that_needs_resource_a()')
        username = self.driver.find_element(By.NAME, 'txtUsername')
        password = self.driver.find_element_by_name('txtPassword')
        LoginButton = self.driver.find_element_by_id('btnLogin')
        username.send_keys("Admin")
        password.send_keys("admin123")
        LoginButton.click()
        self.driver.find_element(By.LINK_TEXT,"Dashboard").is_displayed()

