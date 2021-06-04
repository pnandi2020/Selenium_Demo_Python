'''
Created on Mar 20, 2020
@author: adixit
'''
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2) Navigate to Facebook
browser.maximize_window()
browser.get("https://www.testandquiz.com/selenium/testing.html")

#Select Using Visible Text
element = browser.find_element_by_id("testingDropdown")
drop_down = Select(element)
drop_down.select_by_visible_text("Database Testing")

#Count Number of options
print(len(drop_down.options))
#Get all options from dropdown
all_options = drop_down.options

for options in all_options:
    print(options.text)

time.sleep(5)
browser.close()
