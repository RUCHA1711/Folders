import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1.Goto url
driver.get("http://live.techpanda.org/")
time.sleep(2)

# 2.Click on 'MOBILE' menu
driver.find_element(By.CLASS_NAME,'level0 ').click()
time.sleep(2)

# 3.Click on 'Add to cart' for Sony Experia
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/div[3]/button/span/span').click()
time.sleep(2)

# 4.Click on Edit button
driver.find_element(By.XPATH,'//*[@id="shopping-cart-table"]/tbody/tr/td[4]/ul/li/a').click()
time.sleep(2)

# 5.Edit quantity 
driver.find_element(By.ID,'qty').send_keys('000')
time.sleep(2)

# 6.Click on Update button
driver.find_element(By.XPATH,'//*[@id="product_addtocart_form"]/div[4]/div/div/div[2]/button/span/span').click()

# 7.Verify the error message
error_msg=driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div/div/ul/li/ul/li/span')

if(error_msg):
    print('Verified')
else:
    print('Not verified')

time.sleep(2)

# 8.Click on'Empty cart'
driver.find_element(By.XPATH,'//*[@id="empty_cart_button"]/span/span').click()
time.sleep(2)

# 9.Verify cart is Empty
Empty_cart=driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div/div[1]/h1')

if(Empty_cart):
    print('Verified')
else:
    print('Not verified')