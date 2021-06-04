import json
# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
#Reading data from JSON file
with open('TestData.json') as file:
  data = json.load(file)

# Print the output
print(data)
url=data['url']
print(url)
uname=data['uname']
print(uname)
upass=data['upass']
print(upass)

# Target URL
driver.get(url)
driver.maximize_window()
username = driver.find_element(By.NAME, 'txtUsername')
password = driver.find_element(By.NAME, 'txtPassword')
LoginButton = driver.find_element_by_id('btnLogin')

username.send_keys(uname)
password.send_keys(upass)
LoginButton.click()
driver.close()