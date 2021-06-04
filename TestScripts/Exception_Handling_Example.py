from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# Step 1) Open Firefox
browser = webdriver.Chrome()
# Step 2) Navigate to Facebook
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3) Search & Enter the Email or Phone field & Enter Password
try:
    username = browser.find_element_by_name("txtUsername")
    password = browser.find_element_by_name("txtPassword")
    submit = browser.find_element_by_name("Submit1")
    username.send_keys("Admin")
    password.send_keys("admin123")
    # Step 4) Click Login
    submit.click()
    wait = WebDriverWait(browser, 20)
    page_title = browser.title
    print(page_title)
    assert page_title == "OrangeHRM"
except NoSuchElementException as exception:
    print("Element not found and test failed")
browser.close()

