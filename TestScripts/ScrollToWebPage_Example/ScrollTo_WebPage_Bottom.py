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
#Scroll to Bottom of Page
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
#Scroll to Top of the Page
browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
time.sleep(5)
browser.close()