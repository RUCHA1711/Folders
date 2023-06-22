# Register user with existing email

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

# 1. Navigate to url
driver.get("https://automationexercise.com/")
time.sleep(1)

# 2. Verify that home page is visible successfully
driver.get("https://automationexercise.com/")

if driver.current_url == "https://automationexercise.com/":
    print('Home page is visible successfully.')
else:
    print('Home page is not visible successfully')

# 3. Click on 'Signup / Login' button
driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a/i').click()
time.sleep(1)

# 4. Verify 'New User Signup!' is visible
form=driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div')

if(form):
    print('New User Signup is visible')
else:
    print('New User Signup is visible')

# 5. Enter name and already registered email address
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[2]').click()
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys('Rucha')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]').click()
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys('rucha.tagline@gmail.com')
time.sleep(1)   

# 6. Click 'Signup' button
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/button').click()
time.sleep(1)

# # 7. Verify error 'Email Address already exist!' is visible
Error=driver.find_element(By.XPATH,'/html/body/section/div/div/div[3]/div/form/p')

if(Error):
    print('Email Address already exist!')
else:
    print('Email Address does not exist!')
time.sleep(1)
