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

# 1.Goto url
driver.get("https://testpages.herokuapp.com/styled/challenges/hard-selectors.html")
time.sleep(5)

# 2.Select Me By Id
driver.find_element(By.ID,'select.me.by.id').click()
time.sleep(2)

# 3.