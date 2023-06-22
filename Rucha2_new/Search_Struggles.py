import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Goto url
driver.get("https://seleniumplayground.practiceprobs.com/")
time.sleep(5)

# 2. Click inside the search bar near the top right.
driver.find_element(
    By.XPATH, '/html/body/header/nav/div[2]/div/form/input').click()
time.sleep(1)
# 3. Search for breed
driver.find_element(
    By.XPATH, '/html/body/header/nav/div[2]/div/form/input').send_keys('Breed')
time.sleep(1)

# 4.Return all result page links that contain "Akita Inu".
driver.find_element(By.XPATH,'/html/body/header/nav/div[2]/div/div/div/div/ol/li[2]').click()
time.sleep(1)

links=driver.find_element(By.TAG_NAME,'link')

for li in links:
 print(li.get_attribute('href'))



