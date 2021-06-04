'''
Created on Mar 20, 2020
@author: adixit
'''
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Step 1) Open Firefox
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get("http://the-internet.herokuapp.com/javascript_alerts");
#browser.maximize_window()
browser.find_element_by_css_selector("button[onclick='jsPrompt()']").click()
time.sleep(5)
ActTest = browser.switch_to.alert
ActTest1 = ActTest.text
print(ActTest1)
ExpTest="I am a JS prompt"
assert ActTest1 == ExpTest
ActTest.send_keys("Welcome Abhi")
ActTest.accept()
browser.find_element_by_id("result").text
time.sleep(5)
browser.close()