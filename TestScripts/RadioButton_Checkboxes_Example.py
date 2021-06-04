'''
Created on Mar 20, 2020
@author: adixit
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2) Navigate to Facebook
browser.maximize_window()
browser.get("http://newtours.demoaut.com/")
browser.find_element_by_link_text("SIGN-ON").click()
# Step 3) Search & Enter the Email or Phone field & Enter Password
browser.find_element_by_name("userName").send_keys("testing")
browser.find_element_by_name("password").send_keys("testing")
browser.find_element_by_name("login").click()
#Verify that oneway should not be selected
status = browser.find_element_by_xpath("//input[@value='oneway']").is_selected()
print(status)
browser.find_element_by_xpath("//input[@value='oneway']").click()
#Verify that oneway should not be selected
status = browser.find_element_by_xpath("//input[@value='oneway']").is_selected()
print(status)
browser.find_element_by_name("findFlights").click()
browser.implicitly_wait(5000)
browser.close()
