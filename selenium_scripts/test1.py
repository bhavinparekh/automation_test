import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options

# Set up driver
geckodriver_autoinstaller.install()
chromedriver_autoinstaller.install()


def test(browser, number):
    try:
        if browser == 'chrome':
            chrome_options = Chrome_options()
            # used headless because of docker implementation if you want pop up browser just remove headless tag
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)
        else:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(executable_path='geckodriver', options=options)

        driver.implicitly_wait(100)
        driver.get('http://localhost:9099')
        for i in range(int(number) - 2):
            driver.execute_script(f"window.open('http://localhost:9099', 'tab'+{str(i + 2)});")
            driver.switch_to.window('tab' + str(i + 2))
        return 'all tested successfully'
    except:
        return 'test failed'
