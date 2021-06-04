import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TwoWindows(unittest.TestCase):
    def test_browser_Window(self):
        # open chrome browser
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # set implicit time to 30 seconds
        self.driver.implicitly_wait(5);
        # navigate to the url
        self.driver.get("https://chercher.tech/python/windows-selenium-python")
        # get the Session id of the Parent
        parentGUID = self.driver.current_window_handle
        # click the button to open new window
        self.driver.find_element_by_id("two-window").click()
        time.sleep(5000)
        # get the All the session id of the browsers
        allGUID = self.driver.window_handles
        # pint the title of th epage
        print("Page title before Switching : " + self.driver.getTitle())
        print("Total Windows : " + allGUID.size())
        # iterate the values in the set
        for guid in allGUID:
            # one enter into if blobk if the GUID is not equal to parent window's GUID
            if guid != parentGUID:
                # switch to the guid
                self.driver.switch_to.window(guid)
                # break the loop
                break

        # search on the google page
        self.driver.find_element_by_name("q").send_keys("success")
        # print the title after switching
        print("Page title after Switching to goolge : " + self.driver.getTitle())
        time.sleep(5000);
        # close the browser
        self.driver.close();
        # switch back to the parent window
        self.driver.switch_to.window(parentGUID);
        # print the title
        print("Page title after switching back to Parent: " + self.driver.getTitle());


