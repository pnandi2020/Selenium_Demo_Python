from selenium import webdriver

# WebDriver Chrome
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5000)
driver.maximize_window()

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# to identify element
s = driver.find_element_by_xpath("//input[@type='file']")
# file path specified with send_keys
s.send_keys("C:\\Users\\adixit\\PycharmProjects\\Selenium_Demo\\TestScripts\\Image\\Imagefile.jpg")
