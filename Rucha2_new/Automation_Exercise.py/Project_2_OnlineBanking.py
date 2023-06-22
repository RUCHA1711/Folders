from selenium import webdriver
# from faker import Faker
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Navigate to url
driver.get("https://parabank.parasoft.com/parabank/login.htm")
time.sleep(1)

# fake = Faker()

# 1. Verify that the user can successfully login to the website using correct credentials.
driver.find_element(By.XPATH,'//*[@id="loginPanel"]/form/div[1]/input').click()
driver.find_element(By.XPATH,'//*[@id="loginPanel"]/form/div[1]/input').send_keys('Rucha')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="loginPanel"]/form/div[2]/input').click()
driver.find_element(By.XPATH,'//*[@id="loginPanel"]/form/div[2]/input').send_keys('Admin')
time.sleep(1)

# 2. Verify that the user is unable to login to the website using incorrect credentials.
