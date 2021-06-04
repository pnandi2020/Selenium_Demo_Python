'''
Created on Mar 20, 2020
@author: adixit
'''
import time

from selenium import webdriver
# Step 1) Open Firefox
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2) Navigate to Facebook
browser.get("https://www.testandquiz.com/selenium/testing.html")

#browser.implicitly_wait(5000)
page_title = browser.title
print(page_title)
assert page_title == "Sample Test Page"
browser.find_element_by_id("male").click()
time.sleep(5)
browser.close()