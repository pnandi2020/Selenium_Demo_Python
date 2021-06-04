
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Step 1) Open Firefox
browser = webdriver.Firefox(
    executable_path='C:\\Users\\adixit\\PycharmProjects\\Selenium_Demo\\Browser_Driver\\geckodriver.exe')
# Step 2) Navigate to OrangeHRM

print_options = PrintOptions()
print_options.page_ranges = ['1-2']

browser.get("https://opensource-demo.orangehrmlive.com/")
pageprint = browser.print_page(print_options)
print(pageprint)
browser.close()

