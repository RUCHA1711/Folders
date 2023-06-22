from select import select
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://login-staging.gwork.io/")

# Login
driver.find_element(By.ID, "identity").send_keys("sandy@gmail.com")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "gdpr-cookie-accept").click()
driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(1)
# Performance
driver.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[3]/a/span').click()
time.sleep(5)
# view more button
driver.find_element(By.XPATH,'//*[@id="performance_tab"]/div[1]/div/div[5]/div[6]/div/div[2]/div/div[2]/a').click()
time.sleep(2)
# # view evidence
# driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/a').click()
# time.sleep(4)
# Back to overview
driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div/a').click()
time.sleep(4)
