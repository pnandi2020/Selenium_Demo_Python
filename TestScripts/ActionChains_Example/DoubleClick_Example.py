'''
Created on Mar 20, 2020
@author: adixit
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Step 1) Open Firefox
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2) Navigate to Facebook
browser.get("https://www.testandquiz.com/selenium/testing.html")
action = ActionChains(browser)

dblclick = browser.find_element_by_id("dblClkBtn")

ActionChains(browser).double_click(dblclick).perform()
sleep(5)
ActTest = browser.switch_to.alert
ActTest1 = ActTest.text
print(ActTest1)
ExpTest="hi, JavaTpoint Testing"
assert ActTest1 == ExpTest
ActTest.accept()
browser.close()
