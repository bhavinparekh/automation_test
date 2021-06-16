# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chromedriver_autoinstaller.install()


@given("initialize selenium webdriver")
def step_impl(context):
    # configure Chrome diver

    context.chrome_options = Options()
    context.chrome_options.add_argument('--headless')
    context.chrome_options.add_argument('--no-sandbox')
    context.chrome_options.add_argument('--disable-dev-shm-usage')
    context.driver = webdriver.Chrome(executable_path="chromedriver", options=context.chrome_options)
    context.driver.implicitly_wait(100)

    assert NotImplementedError(u'STEP: Given initialize selenium webdriver')


@when("I launch browser")
def step_impl(context):
    # load web page
    context.driver.get('http://localhost:9099')

    # find video tag
    context.video = context.driver.find_element_by_id('video')
    assert NotImplementedError(u'STEP: When I launch browser')


@step("check video loaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # play video for 10s
    if context.driver.find_element_by_id('video').get_attribute("src"):
        pass
    else:
        raise Exception('Error video not found: Check Charles Proxy')

    assert NotImplementedError(u'STEP: And check video loaded')


@step("play video for {number:d}s")
def step_impl(context, number):
    """
    :param number:
    :type context: behave.runner.Context
    """
    # play video for 10s
    context.video.send_keys(Keys.ENTER)
    time.sleep(number)

    assert NotImplementedError(u'STEP: And play video for 10s')


@step("pause video for {number:d}s")
def step_impl(context, number):
    """
    :param number:
    :type context: behave.runner.Context
    """
    context.video.send_keys(Keys.SPACE)
    time.sleep(number)
    assert NotImplementedError(u'STEP: And pause video for 10s')


@step("seek video for {number:d}s")
def step_impl(context, number):
    """
    :param number:
    :type context: behave.runner.Context
    """
    time_seek = int(number / 5)
    for i in range(time_seek):
        context.video.send_keys(Keys.ARROW_RIGHT)
    assert NotImplementedError(u'STEP: When seek video for 30s')


@then("Test successful and close browser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.quit()
    assert NotImplementedError(u'STEP: Then Test successful and close browser')
