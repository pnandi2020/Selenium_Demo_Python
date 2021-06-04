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
#browser.maximize_window()
browser.get("https://www.google.co.in/")

#Find Links using Tag Name
links = browser.find_elements_by_tag_name("a")

#Count Number of options
print(len(links))
#Print each link name
for i in range(len(links)):
    print(i)
    element = browser.find_elements_by_tag_name("a")[i]
    element.click()
    time.sleep(3)
    if browser.title=="Google":
        print("On Google page")
    else:
        browser.back()
        time.sleep(3)

browser.close()
