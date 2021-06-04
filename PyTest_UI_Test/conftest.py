
# Import the 'modules' that are required for execution

import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver_init(request):
	if request.param == "chrome":
		web_driver = webdriver.Chrome()
		#url ="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
	if request.param == "firefox":
		web_driver = webdriver.Firefox()
		#url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
	request.cls.driver = web_driver
	yield
	web_driver.close()

@pytest.fixture
def app_url():
    url ="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    return url