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
driver.get("https://testpages.herokuapp.com/styled/calculator")
time.sleep(5)

# 2. Number 1
driver.find_element(By.ID,'number1').send_keys('300')
time.sleep(1)

# 3. Minus opeartion
# driver.find_element(By.ID,'function').click()
# time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[1]/select/option[3]').click()
time.sleep(1)

# 4. Number 2
driver.find_element(By.ID,'number2').send_keys('400')
time.sleep(1)

# 5.Calculate
driver.find_element(By.ID,'calculate').click()  
time.sleep(1)

driver.quit()