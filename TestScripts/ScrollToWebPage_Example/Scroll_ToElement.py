'''
Created on Mar 20, 2020
@author: adixit
'''
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Step 1) Open Firefox
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get("https://stackoverflow.com/");
#Scroll from Current position to given Element
target = browser.find_element_by_link_text('Request a demo')
#Scroll to Particular Element
target.location_once_scrolled_into_view
time.sleep(5)
browser.close()