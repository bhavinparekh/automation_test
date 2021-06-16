import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# configure Chrome diver
chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)
driver.implicitly_wait(100)

# load web page
driver.get('http://localhost:9099')

# find video tag
video = driver.find_element_by_id('video')

# play video for 10s
if driver.find_element_by_id('video').get_attribute("src"):
    pass
else:
    raise Exception('Error proxy not found: Check Charles Proxy')
time.sleep(10)

# pause video for 10s
video.send_keys(Keys.SPACE)
time.sleep(10)

# seek video for 30s
time_seek = 5
for i in range(time_seek):
    video.send_keys(Keys.ARROW_RIGHT)

time.sleep(10)
video.send_keys(Keys.SPACE)
print('all tested successfully')
