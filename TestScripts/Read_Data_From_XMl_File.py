from xml.dom import minidom
# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# parse an xml file by name
mydoc = minidom.parse('TestData.xml')

items = mydoc.getElementsByTagName('item')

# one specific item attribute
print('Item attribute:')
print(items[0].attributes['name'].value)
print(items[1].attributes['name'].value)
print(items[2].attributes['name'].value)

# one specific item's data
print('\nItem data:')
Loginbutton = items[0].firstChild.data
username = items[1].firstChild.data
password = items[2].firstChild.data
print(Loginbutton)
print(username)
print(password)
# Target URL
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
driver.maximize_window()
username = driver.find_element(By.NAME, username)
password = driver.find_element(By.NAME, password)
LoginButton = driver.find_element_by_id(Loginbutton)

username.send_keys("Admin")
password.send_keys("admin123")
LoginButton.click()
driver.close()