'''
Created on Mar 20, 2020
@author: adixit
'''
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# Step 1) Open Firefox
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
# Step 2) Navigate to Facebook
browser.get("http://jqueryui.com/resources/demos/droppable/default.html")
action = ActionChains(browser)

drag = browser.find_element_by_id("draggable")
drop = browser.find_element_by_id("droppable")

action.drag_and_drop(drag, drop).perform()
time.sleep(5)
browser.close()
