'''
Created on Mar 20, 2020
@author: adixit
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Step 1) Open Firefox

browser = webdriver.Chrome(ChromeDriverManager().install())
# Step 2) Navigate to Facebook
browser.get("https://opensource-demo.orangehrmlive.com/")

browser.find_element_by_name("txtUsername").send_keys('Admin')
browser.find_element_by_name("txtPassword").send_keys('admin123')
browser.find_element_by_name("Submit").click()
browser.implicitly_wait(5)
browser.find_element_by_link_text('Dashboard').is_displayed()
#Implicit Wait command
#browser.implicitly_wait(7)
page_title = browser.title
print(page_title)
assert page_title == "OrangeHRM"
browser.close()