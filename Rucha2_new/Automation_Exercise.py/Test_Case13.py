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

# 3. Click 'View Product' for any product on home page
driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a').click()
time.sleep(1)

# 4. Verify product detail is opened
driver.get("https://automationexercise.com/product_details/1")

if driver.current_url == "https://automationexercise.com/product_details/1":
    print('Product detail is opened')
else:
    print('Product detail is not opened')

# 5. Increase quantity to 4
driver.find_element(By.ID,'quantity').clear()
time.sleep(2)
driver.find_element(By.ID,'quantity').send_keys('4')
time.sleep(2)

# 6. Click 'Add to cart' button
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button').click()
time.sleep(2)

# 7. Click 'View Cart' button
driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]').click()
time.sleep(1)

# 8. Verify that product is displayed in cart page with exact quantity
cart_quantity=driver.find_element(By.XPATH,'//*[@id="product-1"]/td[4]')

if(cart_quantity):
    print('Product is displayed in cart page with exact quantity')
else:
    print('Product is displayed in cart page with not exact quantity')
time.sleep(1)


