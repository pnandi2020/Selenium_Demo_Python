from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

capabilities = {
  'browserName': 'chrome',
  'browserVersion': '89.0',
  'platformName': 'macOS 10.15',
  'sauce:options': {
  }
}

driver = webdriver.Remote(
    command_executor='https://abhikdixit:d246025c-7be6-497f-9206-2db3dd761350@ondemand.us-west-1.saucelabs.com:443/wd/hub',
    desired_capabilities=capabilities)

driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
username = driver.find_element(By.NAME, 'txtUsername')
password = driver.find_element(By.NAME, 'txtPassword')
LoginButton = driver.find_element_by_id('btnLogin')

username.send_keys("Admin")
password.send_keys("admin123")
LoginButton.click()
driver.quit()