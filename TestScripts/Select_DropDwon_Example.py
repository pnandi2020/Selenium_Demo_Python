'''
Created on Mar 20, 2020
@author: adixit
'''
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
# Step 1) Open Firefox
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2) Navigate to Facebook
browser.get("https://www.testandquiz.com/selenium/testing.html")

page_title = browser.title
print(page_title)
assert page_title == "Sample Test Page"

dropdown= Select(browser.find_element_by_id('testingDropdown'))

firstvalue = dropdown.first_selected_option.text

assert firstvalue == "Automation Testing"
print(firstvalue)

dropdown0= Select(browser.find_element_by_id('testingDropdown'))
dropdown0.select_by_value('Manual')
time.sleep(3)
dropdown1= Select(browser.find_element_by_id('testingDropdown'))
dropdown1.select_by_visible_text('Performance Testing')
time.sleep(3)
dropdown2= Select(browser.find_element_by_id('testingDropdown'))
dropdown2.select_by_index(3)

time.sleep(3)
browser.close()