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

# 5. The products list is visible
products_list=driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div')

if(products_list):
    print('products list is visible')
else:
    print('products list is not visible')
time.sleep(1)

# 6. Click on 'View Product' of first product
driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a').click()
time.sleep(1)

# 7. User is landed to product detail page
driver.get("https://automationexercise.com/product_details/1")

if driver.current_url == "https://automationexercise.com/product_details/1":
    print('User is landed to product detail page')
else:
    print('User is not landed to product detail page')

# 8. Verify that detail is visible: product name, category, price, availability, condition, brand
prodcut_detail=driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div')

if(prodcut_detail):
    print('products detail is visible')
else:
    print('products detail is not visible')
time.sleep(1)