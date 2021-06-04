from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

# Returns height, width, x and y coordinates referenced element
res = driver.find_element(By.NAME, "Submit").rect

print(res)

driver.quit()