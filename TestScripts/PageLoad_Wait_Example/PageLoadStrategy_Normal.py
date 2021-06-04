from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
# Navigate to url
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.quit()