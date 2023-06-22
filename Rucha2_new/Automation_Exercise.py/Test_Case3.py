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

# 4. Verify 'Login to your account' is visible
verify=driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div')

if(verify):
    print('Login to your account')
else:
    print('Not Login to your account')

# 5. Enter incorrect email address and password
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[2]').click()
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys('rucha.tag@gmail.com')
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys('Tag')
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[3]').click()
time.sleep(1)

# 6. Click 'login' button
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/button').click()
time.sleep(1)

# # 7. Verify error 'Your email or password is incorrect!' is visible
Error=driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/p')

if(Error):
    print('Your email or password is incorrect!')
else:
    print('Your email or password is correct!')