from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

# Returns true if element is enabled else returns false
value = driver.find_element(By.NAME, 'Email').is_enabled()
print(value)
if value == True:
    print("Email id is enabled")
    driver.find_element(By.NAME, 'Email').clear()
    driver.find_element(By.NAME, 'Email').send_keys("dixit")
else:
    print("Email id is disabled")

#driver.close()