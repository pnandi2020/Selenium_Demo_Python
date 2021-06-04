from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@given('User has Launched Browser')
def step_impl(context):
    # WebDriver Chrome
    print("Browser Launched")
    # context.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # context.browser = webdriver.Firefox(executable_path='C:\\Users\\adixit\\PycharmProjects\\Selenium_Demo\\Browser_Driver\\geckodriver.exe')


@when('User Navigate to Sign On Page')
def step_impl(context):
    # Step 2) Navigate to OrangeHRM Login Page
    context.browser.get("https://opensource-demo.orangehrmlive.com/")


@when('User enters username and password')
def step_impl(context):
    # Step 3) Enter Username & Password
    context.browser.find_element_by_name("txtUsername").send_keys("Admin")
    context.browser.find_element_by_name("txtPassword").send_keys("admin123")


# Parameters example - Passing UserName and Password


@when('User enters "{username}" and "{password}"')
def step_impl(context, username, password):
    # Step 3) Enter Username & Password
    context.browser.find_element_by_name("txtUsername").send_keys(username)
    context.browser.find_element_by_name("txtPassword").send_keys(password)


@when('User Click on Login Button')
def step_impl(context):
    context.browser.find_element_by_name("Submit").click()


@then('User should logged in and Dashboard page should display')
def step_impl(context):
    page_title = context.browser.title
    print(page_title)
    assert page_title == "OrangeHRM"
    text = context.browser.find_element_by_link_text("Dashboard").text
    assert text == "Dashboard"
    # context.browser.close()


@then('User Click on Welcome Link')
def step_impl(context):
    context.browser.find_element_by_id("welcome").click()
    context.browser.implicitly_wait(3)


@then('User Click on Logout Link')
def step_impl(context):
    context.browser.find_element_by_link_text("Logout").click()


@then('Logout from Application')
def step_impl(context):
    context.execute_steps('then User Click on Welcome Link')
    context.execute_steps('then User Click on Logout Link')


@then('User user travel back to OrangeHRM Login Page')
def step_impl(context):
    context.browser.find_element_by_id("logInPanelHeading").is_displayed()
