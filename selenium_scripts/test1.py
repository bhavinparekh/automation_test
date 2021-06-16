import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up chrome drivet
chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)

# First tab
driver.implicitly_wait(100)
driver.get('http://localhost:9099')

# second tab
driver.execute_script("window.open('http://localhost:9099', 'tab2');")
driver.switch_to.window("tab2")

# third tab
driver.execute_script("window.open('http://localhost:9099', 'tab3');")
driver.switch_to.window("tab3")

# fourth tab
driver.execute_script("window.open('http://localhost:9099', 'tab4');")
driver.switch_to.window("tab4")

print('all tested successfully')
