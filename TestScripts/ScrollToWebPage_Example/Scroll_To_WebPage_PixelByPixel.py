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
#Scroll from Current position to 1500
browser.execute_script("window.scrollTo(0, 1500)")
time.sleep(5)
#Scroll from Current position to 1500
browser.execute_script("window.scrollTo(1500, 3000)")
time.sleep(5)
browser.close()