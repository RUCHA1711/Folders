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
driver.get("https://testpages.herokuapp.com/styled/search")
time.sleep(5)

# 2. Search button
driver.find_element(By.XPATH,'/html/body/div/form/input').click()
time.sleep(1)

# 3. Click on search button
driver.find_element(By.XPATH,'/html/body/div/form/input').click()
time.sleep(2)
