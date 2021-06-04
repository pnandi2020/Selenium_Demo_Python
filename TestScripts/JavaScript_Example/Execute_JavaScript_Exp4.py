from selenium import webdriver

# In This example In this case we capture the element, that we want to work with,
# using javascript provided methods, then declare some actions on it and execute
# this javascript using WebDriver.

# Step 1) Open Firefox
driver = webdriver.Chrome()
# Step 2) Navigate to OrangeHRM
driver.get("https://opensource-demo.orangehrmlive.com/")

username = driver.find_element_by_name("txtUsername")
password = driver.find_element_by_name("txtPassword")
submit = driver.find_element_by_name("Submit")
driver.execute_script("arguments[0].value='Admin';arguments[1].value='admin123';", username, password)
driver.execute_script("arguments[0].click();",submit)
text = driver.execute_script('return document.getElementById("menu_dashboard_index").innerText')
print(text)
driver.quit()
