from selenium import webdriver

# In This example In this case we capture the element, that we want to work with,
# using javascript provided methods, then declare some actions on it and execute
# this javascript using WebDriver.

# Step 1) Open Firefox
driver = webdriver.Firefox()
# Step 2) Navigate to OrangeHRM
driver.get("https://opensource-demo.orangehrmlive.com/")

submit = "document.getElementsByName('Submit')[0].click();"
driver.execute_script(submit)