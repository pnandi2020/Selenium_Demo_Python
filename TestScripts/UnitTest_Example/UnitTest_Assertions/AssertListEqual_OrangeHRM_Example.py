import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestListElements(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # Step 2) Navigate to Facebook
        self.browser.maximize_window()
        self.browser.get("https://www.testandquiz.com/selenium/testing.html")
        self.expected = str(4)
    def test_count_eq(self):
        # Select Using Visible Text
        self.element = self.browser.find_element_by_id("testingDropdown")
        drop_down = Select(self.element)
        drop_down.select_by_visible_text("Database Testing")

        # Count Number of options
        print(len(drop_down.options))
        self.act_count = str(len(drop_down.options))
        """Will succeed"""
        self.assertCountEqual(self.act_count, self.expected)

    '''def test_list_eq(self):
        """Will fail"""
        self.assertListEqual(self.result, self.expected)'''

if __name__ == "__main__":
    unittest.main()