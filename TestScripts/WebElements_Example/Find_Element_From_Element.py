from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
search_form = driver.find_element(By.TAG_NAME, "form")
search_box = search_form.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()
driver.implicitly_wait(30)
driver.close()