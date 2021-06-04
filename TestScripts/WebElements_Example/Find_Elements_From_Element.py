from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

# Get element with tag name 'div'
element = driver.find_element(By.TAG_NAME, 'form')

# Get all the elements available with tag name 'p'
elements = element.find_elements(By.TAG_NAME, 'div')
for e in elements:
    print(e.text)

driver.quit()