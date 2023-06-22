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
driver.get("https://testpages.herokuapp.com/styled/validation/input-validation.html")
time.sleep(5)

# 2.First Name
driver.find_element(By.ID,'firstname').send_keys('Tester')
time.sleep(1)

# 3.Last Name
driver.find_element(By.ID,'surname').send_keys('Tagline1234')
time.sleep(1)

# 4.Age
driver.find_element(By.ID,'age').send_keys('20')
time.sleep(1)

# 5.Country
driver.find_element(By.XPATH,'//*[@id="country"]/option[78]').click()
time.sleep(1)

# 6.Submit button
driver.find_element(By.XPATH,'/html/body/div/div[3]/form/input[4]').click()
time.sleep(1)