from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Step 1) Open Firefox
browser = webdriver.Firefox(
    executable_path='C:\\Users\\adixit\\PycharmProjects\\Selenium_Demo\\Browser_Driver\\geckodriver.exe')
#Get WindowSize before execution.

# Access each dimension individually
width = browser.get_window_size().get("width")
height = browser.get_window_size().get("height")

# Or store the dimensions and query them later
size = browser.get_window_size()
width1 = size.get("width")
height1 = size.get("height")
print(width1)
print(height1)

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

