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

# 3. Click 'Cart' button
driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]').click()
time.sleep(1)

# 3. Scroll down to footer
driver.execute_script('window.scrollBy(0,9000)')
time.sleep(5)

# 4. Verify text 'SUBSCRIPTION'
subscription=driver.find_element(By.XPATH,'//*[@id="success-subscribe"]')

if(subscription):
    print('Subscription text is visible')
else:
    print('Subscription text is not visible')
time.sleep(1)

# 5. Enter email address in input and click arrow button
driver.find_element(By.ID,'susbscribe_email').click()
driver.find_element(By.ID,'susbscribe_email').send_keys('rucha.tagline@gmail.com')
driver.find_element(By.ID,'subscribe').click()
time.sleep(1)

# 6. Verify success message 'You have been successfully subscribed!' is visible
success_message=driver.find_element(By.XPATH,'//*[@id="success-subscribe"]/div')

if(success_message):
    print('You have been successfully subscribed!')
else:
    print('You have been successfully subscribed!')
time.sleep(1)
