'''
Created on Mar 20, 2020
@author: adixit
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2) Navigate to Facebook
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_name("txtUsername")
password = browser.find_element_by_name("txtPassword")
submit = browser.find_element_by_name("Submit")
username.send_keys("Admin")
password.send_keys("admin123")
# Step 4) Click Login
submit.click()
# Explicit Wait command
wait = WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Dashboard")))

page_title = browser.title
print(page_title)
assert page_title == "OrangeHRM"
browser.find_element_by_link_text("Admin").click()
browser.close()


