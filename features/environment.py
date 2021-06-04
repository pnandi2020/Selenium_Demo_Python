from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    # define browser instance
    # WebDriver Chrome
    context.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.browser.implicitly_wait(2)


def after_all(context):
    context.browser.quit()


#def after_scenario(context):
    #context.browser.refresh()
