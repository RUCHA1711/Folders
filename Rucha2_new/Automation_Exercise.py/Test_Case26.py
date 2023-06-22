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

# 3. Scroll down to bottom
driver.execute_script('window.scrollBy(0,9000)')
time.sleep(5)

# 4. Verify 'SUBSCRIPTION' is visible'
subscription=driver.find_element(By.XPATH,'//*[@id="success-subscribe"]')

if(subscription):
    print('Subscription text is visible')
else:
    print('Subscription text is not visible')
time.sleep(1)

# 5. Scroll up page to top
driver.execute_script('window.scrollBy(0,-9000)')
time.sleep(10)

# 6. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
page_is_scrolled_up=driver.find_element(By.XPATH,'//*[@id="slider-carousel"]/div/div[1]/div[1]/h2')

if(page_is_scrolled_up):
    print('Page is scrolled up and Full-Fledged practice website for Automation Engineers text is visible on screen')
else:
    print('Page is not scrolled up and Full-Fledged practice website for Automation Engineers text is not visible on screen')
time.sleep(1)

