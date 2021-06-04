import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

# Launch Browser

#browser = webdriver.Ie(IEDriverManager().install())
#browser = webdriver.Chrome(ChromeDriverManager().install())
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser = webdriver.Edge(EdgeChromiumDriverManager().install())
# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_name("txtUsername")
password = browser.find_element_by_name("txtPassword")
submit = browser.find_element_by_name("Submit")
#Screenshot at object Level
#submit.screenshot_as_png("SubmitButton.png")
username.send_keys("Admin")
password.send_keys("admin1234")
time.sleep(2)

#Save Screenshot at browser level
#browser.save_screenshot("InvalidCredentials.png")
# Step 4) Click Login
submit.click()
wait = WebDriverWait(browser, 20)
page_title = browser.title
print(page_title)
assert page_title == "OrangeHRM"
browser.close()
