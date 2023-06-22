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

# 3. Click on 'Products' button
driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]').click()
time.sleep(1)

# 4. Verify user is navigated to ALL PRODUCTS page successfully
driver.get("https://automationexercise.com/products")

if driver.current_url == "https://automationexercise.com/products":
    print('User is navigated to ALL PRODUCTS page successfully')
else:
    print('User is navigated to ALL PRODUCTS page successfully')

# 5. Enter product name in search input and click search button
driver.find_element(By.ID,'search_product').click()
driver.find_element(By.ID,'search_product').send_keys('DRESS')
driver.find_element(By.ID,'submit_search').click()
time.sleep(1)

# 6. Verify 'SEARCHED PRODUCTS' is visible
driver.get('https://automationexercise.com/products?search=DRESS')

if driver.current_url == "https://automationexercise.com/products?search=DRESS":
    print('Serached Products is visible')
else:
    print('Searched Products is not visible')
    
# 7. Verify all the products related to search are visible
searched_products=driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div')

if(searched_products):
    print('Products related to search are visible')
else:
    print('Products related to search are not visible')
time.sleep(1)
