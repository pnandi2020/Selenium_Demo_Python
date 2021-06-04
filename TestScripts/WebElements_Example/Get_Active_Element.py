from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

# Get attribute of current active element
attr = driver.switch_to.active_element.get_attribute("value")
print(attr)
driver.close()