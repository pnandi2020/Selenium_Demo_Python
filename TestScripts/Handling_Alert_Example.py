'''
Created on Mar 20, 2020
@author: adixit
'''
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Step 1) Open Firefox
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get("https://netbanking.hdfcbank.com/netbanking/");
browser.maximize_window()
browser.switch_to.frame("login_page")
browser.find_element_by_xpath("//img[@alt='continue']").click()
time.sleep(5)
ActTest = browser.switch_to.alert
ActTest1 = ActTest.text
print(ActTest1)
ExpTest="Customer ID  cannot be left blank."
assert ActTest1 == ExpTest
#assert ActTest1 not in ExpTest
ActTest.accept()
time.sleep(5)
browser.close()