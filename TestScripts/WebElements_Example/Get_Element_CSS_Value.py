from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

# Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element_by_id("btnLogin").value_of_css_property('color')

print(cssValue)

driver.quit()