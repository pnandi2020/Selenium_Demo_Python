'''
Created on Mar 20, 2020
@author: adixit
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#Options Module from Python Selenium Package
opts = Options()
# Running in headless mode
#opts.__setattr__("headless",True)
# Running in Incognito Mode
opts.add_argument("incognito")
#assert opts.headless
# Step 1) Open Firefox
#browser = webdriver.Firefox(executable_path='C://Users//adixit//PycharmProjects//Selenium_Demo//Browser_Driver//geckodriver.exe',options=opts)
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=opts)
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_name("txtUsername")
password = browser.find_element_by_name("txtPassword")
submit = browser.find_element_by_name("Submit")
username.send_keys("Admin")
password.send_keys("admin123")
# Step 4) Click Login
submit.click()
wait = WebDriverWait(browser, 20)
page_title = browser.title
print(page_title)
assert page_title == "OrangeHRM"
browser.close()
