import unittest
import HTMLTestRunner

# get the directory path to output report file
from TestScripts.UnitTest_Example.UnitTest_Decorator.UnitTest_Setup_TearDown import SearchText
from TestScripts.UnitTest_Example.UnitTest_Decorator.UnitTest_Setup_TearDown_Class_Level import OrangeHRM_Login_Logout

# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(OrangeHRM_Login_Logout)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(title='Test Summary Report', description='Execution of Smoke Tests', report_name='Smoke Test Report')

# run the suite using runner object, with customized details.
runner.run(test_suite)
# run the suite using HTMLTestRunner, which will have default file name
# report name with date and time
#HTMLTestRunner.HTMLTestRunner(verbosity=2).run(test_suite)
