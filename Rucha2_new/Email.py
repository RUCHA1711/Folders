import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1.Goto url
driver.get("http://live.techpanda.org/index.php/backendlogin")
time.sleep(2)

# 2.Login the credentials provided
driver.find_element(By.ID,'username').send_keys('user01')
time.sleep(1)
driver.find_element(By.ID,'login').send_keys('guru99com')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[5]/input').click()
time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="message-popup-window"]/div[1]/a/span').click()
time.sleep(1)

# 3.Go to Sales and click Export button
driver.find_element(By.XPATH,'//*[@id="nav"]/li[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="nav"]/li[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'').click()
time.sleep(100)
